from django.urls import path,re_path

from . import consumers
from . import consumers1


websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    re_path(r'^ws/chat/(?P<room_name>[\w-]+)/', consumers1.ChatConsumer.as_asgi()),
]