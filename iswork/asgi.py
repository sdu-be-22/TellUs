import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing
import privateRoom.routing 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iswork.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    "websocket": AuthMiddlewareStack(
        URLRouter(
            privateRoom.routing.websocket_urlpatterns +
            room.routing.websocket_urlpatterns
        )
    ),
})
