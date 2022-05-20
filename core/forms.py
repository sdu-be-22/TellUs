from django import forms
from django.forms import Textarea
from .models import Articles, Comments, UserProfile
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm , UserChangeForm , PasswordChangeForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length = 25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required = False, widget = forms.Textarea)
    captcha = CaptchaField()

class EditProfileName(forms.Form): 
    name = forms.CharField(max_length = 25)
    

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('name','text', 'picture')
        # labels = {
        #     "name": _(""),
        #     "text": _(""),
        #     "picture": _("")
        # }
    def __init__(self,*args,**kwargs):
        super(ArticleForm, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            



class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows':5})
        


class EditProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    class Meta:
        model=User
        fields=('username','first_name' , 'last_name' , 'email' ,'last_login' ,'date_joined')
        
class UpdateProfilePhoto(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model  = UserProfile
        fields = ('image',)

        
class UpdateProfilePhoto(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model  = UserProfile
        fields = ('picture',)


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type': 'password'}))


    class Meta:
        model=User
        fields=('old_password' , 'new_password1', 'new_password2')
