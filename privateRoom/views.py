from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import ChatModel
from core.models import UserProfile

User = get_user_model()

@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    users_profile = UserProfile.objects.get(user_id=request.user.id)
    user_followers= users_profile.followers.all()

    # for  user_follower in  user_followers:
    #     print(user_follower)
    #     users = User.objects.filter(username=user_follower)

    return render(request, 'privateChat/chats.html', context={'users': users, "user_followers": user_followers})

@login_required
def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    users_profile = UserProfile.objects.get(user_id=request.user.id)
    user_followers = users_profile.followers.all()

    # for user_follower in user_followers:
    #      users = User.objects.filter(username=user_follower.user)

    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'privateChat/main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs, "user_followers": user_followers})
