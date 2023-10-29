from rest_framework import serializers
from .models import *

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('name', 'profile_picture', 'id')


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'group', 'is_admin_only')

class VideoChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoChannel
        fields = ('id', 'name', 'group', 'is_admin_only')

class GroupMemberSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    group_id = serializers.IntegerField()


    def create(self, validated_data):
        return GroupMember.objects.create(**validated_data)

class GroupMessageSerializer(serializers.ModelSerializer):
    sender_username=serializers.SerializerMethodField()
    sender_profile_picture = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    class Meta:
        model=GroupMessage
        fields=['message','sender_username', 'send_at', 'sender_profile_picture', 'user_id']
    
    def get_sender_username(self,obj):
        return obj.sender.username
    
    def get_sender_profile_picture(self, obj):
        if obj.sender.profile_picture:
            return obj.sender.profile_picture.url 
        return None

    def get_user_id(self, obj):
        return obj.sender.id