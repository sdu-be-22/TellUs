from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.db.models import Q
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Articles(models.Model , HitCountMixin):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Article owner', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Post name:')
    text = RichTextField(blank=True, null=True)
    # slug = models.SlugField(unique=True, max_length=100)
    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')


    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super(Articles, self).save(*args, **kwargs)
    
    # class Meta:
    #     verbose_name='Статью'
    #     verbose_name_plural='Статьи'

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

