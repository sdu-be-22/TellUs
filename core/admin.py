from django.contrib import admin
from core.models import Articles, Likes, Comments, Notification,  UserProfile, ThemePage


# Register your models here.
admin.site.register(Articles)
admin.site.register(Likes)
admin.site.register(Comments) 
admin.site.register(Notification)
admin.site.register(UserProfile)
admin.site.register(ThemePage)
