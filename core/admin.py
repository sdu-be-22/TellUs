from django.contrib import admin
from core.models import Articles, Likes, Comments, Notification, Profile


# Register your models here.
admin.site.register(Articles)
admin.site.register(Likes)
admin.site.register(Comments) 
admin.site.register(Notification)
admin.site.register(Profile)