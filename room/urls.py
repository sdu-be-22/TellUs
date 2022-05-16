from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    # path("~chats/", views.index, name="chats"),
    # path('~chat/<str:username>/', views.chatPage, name='chat'),
]