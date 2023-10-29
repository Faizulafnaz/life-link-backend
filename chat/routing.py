from django.urls import path
from .consumer import PersonalChatConsumer, GroupChatConsumer

websocket_urlpatterns=[
    path('ws/chat/<int:id>/',PersonalChatConsumer.as_asgi()),
    path('ws/chat/group/<int:room_name>/',GroupChatConsumer.as_asgi()),
]