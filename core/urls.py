from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail_page'),
    path('edit-page', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_page'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
    path('password_reset/' , views.password_reset_form, name='password_reset'),
    path('search/', views.search, name='search'), 
    path('like/<int:pk>', views.like, name='likes'),
    path('notifs_json', views.JsonList.as_view(), name='json_notif_lists'),
    path('ajax_notification/', views.NotificationCheck.as_view(), name='ajax_notification'),
    #ajax
    path('update_comment_status/<int:pk>/<slug:type>', views.update_comment_status, name='update_comment_status')
]
