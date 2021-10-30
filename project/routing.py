"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
# from Pendent.project.newapp.views import index
# from djangochannelsrestframework.consumers import view_as_consumer

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
# from . import consumers
from newapp.consumers import *

from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
# from . import views

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_asgi_application()


# ws_patterns=[
#     path('ws/tt/', DashConsumer.as_asgi()),
# ]

# application = ProtocolTypeRouter({
#     # 'http': get_asgi_application(),
#     'websocket': URLRouter(ws_patterns)


# })

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('ws/chating/', ChatConsumer), # Using asgi
                ]
            )
            
        )
    )})