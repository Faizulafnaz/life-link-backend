from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Groups, Channel, GroupMessage, VideoChannel, VoiceChannel
from .serializers import GroupsSerializer, ChannelSerializer, GroupMemberSerializer, GroupMessageSerializer, VideoChannelSerializer, VoiceChannelSerializer
from rest_framework.filters import SearchFilter

class CreateGroupView(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [SearchFilter]
    search_fields = ['name']

class CreateChannelView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    parser_classes = (MultiPartParser, FormParser)

class CreateVideoChannelView(generics.ListCreateAPIView):
    queryset = VideoChannel.objects.all()
    serializer_class = VideoChannelSerializer
    parser_classes = (MultiPartParser, FormParser)

class CreateVoiceChannelView(generics.ListCreateAPIView):
    queryset = VideoChannel.objects.all()
    serializer_class = VoiceChannelSerializer
    parser_classes = (MultiPartParser, FormParser)

class GroupVoiceChannelView(generics.ListAPIView):
    serializer_class = VideoChannelSerializer
    def get_queryset(self):
        id = int(self.kwargs['id'])
        return VoiceChannel.objects.filter(group=id)

class GroupVideoChannelView(generics.ListAPIView):
    serializer_class = VideoChannelSerializer
    def get_queryset(self):
        id = int(self.kwargs['id'])
        return VideoChannel.objects.filter(group=id)

class UserGroupsListView(generics.ListAPIView):
    serializer_class = GroupsSerializer
    def get_queryset(self):
        user = int(self.kwargs['user_id'])
        return Groups.objects.filter(groupmember__user=user)

class GroupChannelView(generics.ListAPIView):
    serializer_class = ChannelSerializer
    def get_queryset(self):
        id = int(self.kwargs['id'])
        return Channel.objects.filter(group=id)

class GroupMemberCreateView(generics.CreateAPIView):
    serializer_class = GroupMemberSerializer

class GroupsDetailsView(generics.ListAPIView):
    serializer_class = GroupsSerializer
    def get_queryset(self):
        id = int(self.kwargs['id'])
        return Groups.objects.filter(id=id)

class ChannelDetailsView(generics.ListAPIView):
    serializer_class = ChannelSerializer
    def get_queryset(self):
        id = int(self.kwargs['id'])
        return Channel.objects.filter(id=id)

class PreviousGroupMessagesView(generics.ListAPIView):
    serializer_class = GroupMessageSerializer

    def get_queryset(self):
        channel = int(self.kwargs['channel'])
        queryset = GroupMessage.objects.filter(
            channel =  channel
        )
        return queryset