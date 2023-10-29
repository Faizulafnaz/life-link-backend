from django.shortcuts import render
from .models import DirectMessage
from .serializer import MessageSerializer, UserReadOnlySerializer, ChatListSerializer
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from authentication.models import CustomUser
from authentication.serializer import UserRegister
from rest_framework.filters import SearchFilter

# Create your views here.
class PreviousMessagesView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user1 = int(self.kwargs['user1'])
        user2 = int(self.kwargs['user2'])

        thread_suffix = f"{user1}_{user2}" if user1 > user2 else f"{user2}_{user1}"
        thread_name = 'chat_'+thread_suffix
        queryset = DirectMessage.objects.filter(
            thread_name=thread_name
        )
        return queryset

class GetUserDetails(APIView):
    def get(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)
        serializer = UserReadOnlySerializer(user)
        return Response(serializer.data)

class UserList(ListCreateAPIView):
    queryset = CustomUser.objects.all().exclude(is_superuser=True)
    serializer_class = UserRegister
    filter_backends = [SearchFilter]
    search_fields = ['email', 'username']

class ChatListView(ListAPIView):
    serializer_class = ChatListSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['user_id'])
        distinct_senders = DirectMessage.objects.filter(receiver__id=user_id).values('sender__username').distinct()
        distinct_receivers = DirectMessage.objects.filter(sender__id=user_id).values('receiver__username').distinct()

        distinct_usernames = set()
        for entry in distinct_senders:
            distinct_usernames.add(entry['sender__username'])

        for entry in distinct_receivers:
            distinct_usernames.add(entry['receiver__username'])
        return distinct_usernames

