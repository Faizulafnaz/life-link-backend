from django.urls import path, include
from .views import *

urlpatterns = [
    path("user-previous-chats/<int:user1>/<int:user2>/", PreviousMessagesView.as_view()),
    path('getuserdetails/<int:user_id>/',GetUserDetails.as_view(),name='UserDetails'),
    path('user-list/',UserList.as_view(),name='user_list'),
    path("chat-list/<int:user_id>/", ChatListView.as_view()),
]