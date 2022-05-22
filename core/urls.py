from django.contrib import admin
from django.urls import path, re_path
from core import views
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('detail/<int:pk>/', views.HomeDetailView.as_view(), name='detail_page'),
    path('edit-page/', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>/', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>/', views.ArticleDeleteView.as_view(), name='delete_page'),
    path('login/', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register/', views.RegisterUserView.as_view(), name='register_page'),
    path('logout/', views.MyProjectLogout.as_view(), name='logout_page'),
    path('<str:post_name>/share/', views.post_share, name='post_share'),
    path('search/', views.searchArticles, name = "search_results"),
    path('like/<int:pk>/', views.like, name='likes'),
    path('notifs_json/', views.JsonList.as_view(), name='json_notif_lists'),
    path('ajax_notification/', views.NotificationCheck.as_view(), name='ajax_notification'),
    path('edit_profile/', views.profileEdit ,name ='edit_profile' ),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/followers/add', views.AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', views.RemoveFollower.as_view(), name='remove-follower'),
    # path('password/' , auth_views.PasswordChangeView.as_view(template_name='change-password.html')) ,
    path('password/' , PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success/' , views.password_success, name ="password_success"),
    #url password reset application urls.py
    path('password_reset/', views.password_reset_form, name="password_reset"),
    #ajax
    path('update_comment_status/<int:pk>/<slug:type>/', views.update_comment_status, name='update_comment_status'),
    #path("post/<int:post_pk>/comment/reply/<int:pk>", views.CommentReplyView.as_view(), name="comment-reply"),


]
