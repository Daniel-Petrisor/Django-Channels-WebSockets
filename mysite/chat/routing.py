from django.urls import path
from .consumers import ChatConsumers

websocket_urlpatterns = [
    path('ws/socket-server/', ChatConsumers.as_asgi())
]