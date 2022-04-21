from datetime import datetime, timezone
import datetime
from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.db.models import Q

# Create your models here.


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Article owner', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Post name:')
    text = models.TextField(verbose_name='Text')
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     verbose_name='Статью'
    #     verbose_name_plural='Статьи'


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='post_like') 
    

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete = models.CASCADE, verbose_name='Post', blank = True, null = True,related_name='comments_articles')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Comment author', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Text comment')
    status = models.BooleanField(verbose_name='Post Visibility', default=False)
    # objects  = StatusFilterComments() 
    
    
class Notification(models.Model):
    notification_type = models.IntegerField()
    user_to = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    user_from = models.ForeignKey(User, related_name='notification_from',on_delete=models.CASCADE,  null=True)
    post = models.ForeignKey(Articles, related_name="+", on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comments, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    likes = models.ForeignKey(Likes, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(datetime.datetime.now) 
    user_has_seen = models.BooleanField(default=False)