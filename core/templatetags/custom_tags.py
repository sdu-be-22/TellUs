from django import template
from ..models import Notification

register = template.Library()

@register.inclusion_tag('notification.html', takes_context=True)
def show_notifications_new(context):
    read = False
    user = context['request'].user
    notifications = Notification.objects.filter(user_to = user).exclude(user_has_seen=True).order_by('-date')
    for i in notifications:
            i.user_has_seen = True
            i.save()

    # for i in notifications: 
    #     if(i.user_has_seen == False):
    #        notifications.update(user_has_seen = True)
    return {'notifications': notifications, 'read' : read}


@register.inclusion_tag('index.html', takes_context=True)
def change_language(context):
    lang = context['request'].post['form-select']
    
    

@register.inclusion_tag('notification.html', takes_context=True)
def show_notifications_old(context):
    read = True
    user = context['request'].user
    notifications = Notification.objects.filter(user_to = user, user_has_seen= True).order_by('-date')
    return {'notifications' : notifications, 'read' : read}

@register.simple_tag
def total_unread_notifs(r_user):
    user = r_user
    total = Notification.objects.filter(user_to=user, user_has_seen=False).count()
    return total

@register.simple_tag
def notif_seen(r_user):
    user = r_user
    unseen = Notification.objects.filter(user_to=user, user_has_seen=False)
    for i in unseen:
        i.user_has_seen = True
        i.save()
        total_unread_notifs(r_user)
