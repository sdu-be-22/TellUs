from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="chats"),
    path('<str:username>/', views.chatPage, name='chat'),
]