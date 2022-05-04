"""iswork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('', include('core.urls')),
    path("room/", include("room.urls")),
    path('admin/', admin.site.urls),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password-reset-form.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password-reset-done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password-reset-confirm.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password-reset-complete.html"), 
        name="password_reset_complete"),
    path('captcha/', include('captcha.urls')),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 