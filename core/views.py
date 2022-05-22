from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
import datetime
from unittest import loader
from django.utils.decorators import method_decorator
from .models import Articles,Comments, Likes, Notification, UserProfile, ThemePage
from django.views.generic import ListView, DetailView,CreateView, UpdateView,DeleteView
from django.views.generic.edit import FormMixin
from .forms import ArticleForm, AuthUserForm, RegisterUserForm, CommentForm, EmailPostForm, ProfileNameEmail, PasswordChangingForm, UpdateProfilePhoto
from django.urls import reverse, reverse_lazy 
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models import Q;
from django.utils import timezone
from hitcount.views import HitCountDetailView
from django.contrib.auth.forms import UserChangeForm ,  PasswordChangeForm
from django.contrib.auth.views import PasswordChangeForm
from django.views import generic
from django.utils.translation import gettext as _
from .forms import EditProfileForm , PasswordChangingForm, UpdateProfilePhoto



def post_list(request):
    go_to = _('go to article')
    popular_post = _('Popular posts')
    object_list = Articles.objects.all().order_by('-likes')
    paginator = Paginator(object_list, 3)

    page = request.GET.get('page')

    try: 
        list_articles = paginator.page(page)
    except PageNotAnInteger:
        list_articles = paginator.page(1)
    except EmprtPage:
        list_articles = paginator.page(paginator.num_pages)
    return render(request, "main.html", {'list_articles': list_articles, 'page':page, "object_list": object_list, 'go_to': go_to, "popular_post": popular_post})


def post_share(request, post_name):
    articles = get_object_or_404(Articles, name=post_name)
    sent = False

    messages.success(request, 'Your profile is updated successfully')
    if request.method == "POST":
        form = EmailPostForm(request.POST)  
        if(form.is_valid()): 
            cd = form.cleaned_data
            subject_url = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post_name)

            message = "Read '{}' \n\n{}\'s comments: {}".format(post_name, cd['name'], cd['comments'])
            send_mail(subject_url, message, 'loarsen9@email.com', [cd['to']])
    else: 
        form = EmailPostForm()

    return render(request, 'share.html', {
                            'articles': articles,
                            'form':  form,
                            'sent': sent})


def password_reset_form(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        profile_name_email = ProfileNameEmail(request.POST)

        if password_reset_form.is_valid() and profile_name_email.is_valid():
            data = password_reset_form.cleaned_data['email']
            name = profile_name_email.cleaned_data["username"]
            associated_users = User.objects.filter(Q(username = name))
            print(associated_users)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.txt"
                    c = {
                    "email": user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject,  email, 'loarsen9@gmail.com' , [data])
                        messages.success(request, 'Check your email')
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    
                    #return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    profile_name_email = ProfileNameEmail()
    return render(request=request, template_name="accounts/password-reset-form.html", context={"password_reset_form":password_reset_form, "profile_name_email":profile_name_email})




# search
def searchArticles(request):
    query = request.GET.get('q') if request.method!= None else ''
    results = Articles.objects.filter(
        Q(name__icontains=query) |
        Q(text__icontains=query)
    )
    if query == '':
        results = Articles.objects.all()
    return render(request, "search_result.html", {'list_articles': results})




@login_required
def update_comment_status(request, pk, type):
    item = Comments.objects.get(pk=pk)
    if request.user != item.article.author:
        return HttpResponse('deny')

    if request.user == None:
        return redirect('login_page')
        
    if type == 'delete':
        item.delete()
        return HttpResponse()
    
    return HttpResponse('1')


@login_required
def like(request, pk):
  
    user = request.user
    post = Articles.objects.get(id=pk)
    post_owner = post.author
    notification_type = 1
    current_likes = post.likes 
    liked = Likes.objects.filter(user=user, post=post)
    
    
    if not liked: 
        like = Likes.objects.create(user=user, post=post)
        like.save()
        current_likes = current_likes + 1 
        notification = Notification.objects.create(notification_type=notification_type, 
                                                   user_to = post_owner,
                                                   user_from=user,
                                                   post=post,
                                                   likes=like,
                                                   date = timezone.now())
        notification.save()
        
    else:
        Likes.objects.filter(user=user, post=post).delete()
        Notification.objects.filter(notification_type=notification_type, 
                                                   user_to = post_owner,
                                                   user_from=user,
                                                   post=post).delete()
        current_likes = current_likes - 1
    
    
    
    post.likes=current_likes
    post.save()
    return HttpResponseRedirect(reverse('detail_page', args=[pk]))

@login_required 
def profileEdit(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance = request.user)
        profile_form  = UpdateProfilePhoto(request.POST, request.FILES,instance = request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='edit_profile')
    else: 
        user_form = EditProfileForm(instance= request.user)
        profile_form = UpdateProfilePhoto(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'user_form' : user_form, 'profile_form' : profile_form})

    

class HomeListView(ListView):
    pass


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
        
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


# @login_required(login_url='login_page')
class HomeDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'get_article'
    form_class = CommentForm
    # success_msg = 'Comment successfully created, please wait for moderation'
    
    
    def get_success_url(self):
        return reverse_lazy('detail_page', kwargs={'pk':self.get_object().id})
    
    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        notification = Notification.objects.create(notification_type=2, 
                                                   user_to = self.object.article.author, 
                                                   user_from = self.object.author,
                                                   post = self.object.article,
                                                   comment = self.object,
                                                   date = timezone.now())
        notification.save()
        return super().form_valid(form)
    

    

class ArticleCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Post created' 
    def get_context_data(self,**kwargs):
        kwargs['list_articles'] = Articles.objects.all().order_by('-id')
        object_list = kwargs['list_articles']
        paginator = Paginator(object_list, 3)

        page = self.request.GET.get('page')

        try: 
            kwargs['list_articles'] = paginator.page(page)
        except PageNotAnInteger:
            kwargs['list_articles'] = paginator.page(1)
        except EmprtPage:
            kwargs['list_articles'] = paginator.page(paginator.num_pages)
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    

class ArticleUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin,UpdateView):
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')
    success_msg = _('Post successfully updated')
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs



class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'User successfully created'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid

class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = _('Post removed')
    def post(self,request,*args,**kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class JsonList(View): 
    def get(self, *args, **kwargs):
        notifs = list(Notification.objects.filter(user=self.request.user))
        return JsonResponse(self, {'data' : notifs}, safe=False)

@method_decorator(login_required, name='dispatch')
class NotificationCheck(View):
    def get(self, request):
        return HttpResponse(Notification.objects.filter(user_has_seen = False, user_to=request.user).count()) 


class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    # from_class=PasswordChangeView
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'password_success.html', {}) 



class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=User.objects.get(pk=pk))
        user = profile.user
        #posts= ""
        posts = Articles.objects.filter(author=user)

        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
        }

        return render(request, 'profile.html', context)


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)
        return redirect('profile', pk=profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        return redirect('profile', pk=profile.pk)