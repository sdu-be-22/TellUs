from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import ChatModel


User = get_user_model()

@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'privateChat/chats.html', context={'users': users})

@login_required
def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'privateChat/main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
