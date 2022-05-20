from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.db.models import Q
from datetime import datetime, timezone
import datetime
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Articles(models.Model, HitCountMixin):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Article owner', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Post name:')
    picture = models.ImageField(upload_to="images",blank=True, null=True,  default='images/default/defaultPost.png')
    text = RichTextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
   
    def __str__(self):    
        return self.name 


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/user_profiles', default='images/default/defaultProfile.png', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): 
    if created: 
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs): 
    instance.profile.save()


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete = models.CASCADE, verbose_name='Post', blank = True, null = True,related_name='comments_articles' )
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Comment author', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Text comment')
    status = models.BooleanField(verbose_name='Post Visibility', default=False)
    # objects  = StatusFilterComments()


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='post_like') 
    

class Notification(models.Model):
    notification_type = models.IntegerField()
    user_to = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    user_from = models.ForeignKey(User, related_name='notification_from',on_delete=models.CASCADE,  null=True)
    post = models.ForeignKey(Articles, related_name="+", on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comments, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    likes = models.ForeignKey(Likes, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(datetime.datetime.now) 
    user_has_seen = models.BooleanField(default=False)


class ThemePage(models.Model):
    color = models.CharField(max_length=1000)
    user=models.CharField(max_length=1000)

    def __str__(self):
        return self.user