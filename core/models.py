from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.db.models import Q

# Create your models here.
class Articles(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Article owner', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Post name:')
    picture = models.ImageField(upload_to="images",blank=True,null=True,  default='images/default/images.png')
    text = models.TextField(verbose_name='Text')
    
    def __str__(self):
        return self.name


class StatusFilterComments(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(status=False, author = get_current_user()) | Q(status=False, article__author=get_current_user()) | Q(status=True))
    


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete = models.CASCADE, verbose_name='Post', blank = True, null = True,related_name='comments_articles' )
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Comment author', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Text comment')
    status = models.BooleanField(verbose_name='Post Visibility', default=False)
    objects  = StatusFilterComments()

