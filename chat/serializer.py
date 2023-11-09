from rest_framework import serializers
from .models import *
from authentication.serializer import UserRegister
from .models import DirectMessage

# class DirectMessageSerializer(serializers.ModelSerialize):
#     sender_details = UserRegister(read_only = True)
#     reciever_details = UserRegister(read_only = True)
#     class Meta:
#         model = DirectMessage
#         field = ['id', 'user' , 'sender', 'reciever', 'is_read', 'send_at', 'sender_details', 'reciever_details']

class MessageSerializer(serializers.ModelSerializer):
    sender_username=serializers.SerializerMethodField()

    class Meta:
        model=DirectMessage
        fields=['message','sender_username', 'send_at']

    def get_sender_username(self,obj):
        return obj.sender.username


class ChatListSerializer(serializers.ModelSerializer):

    profile_picture=serializers.SerializerMethodField()
    username=serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    unread = serializers.SerializerMethodField()

    class Meta:
        model=DirectMessage
        fields=['username', 'profile_picture', 'id', 'unread']

    def get_username(self,obj):
        return obj
    
    def get_profile_picture(self, obj):
        user = CustomUser.objects.get(username=obj)
        if user.profile_picture:
            return 'http://127.0.0.1:8000' + user.profile_picture.url
    
    def get_id(self, obj):
        user = CustomUser.objects.get(username=obj)
        return user.id
    
    def get_unread(self, obj):
        user = self.context.get('user_id')
        unread_count = DirectMessage.objects.filter(receiver=int(user), sender__username=obj, is_read=False).count()
        return unread_count


class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'id', 'is_varified', 'otp', 'date_of_birth', 'profile_picture', 'first_name', 'last_name']

class MessageRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageRequest
        fields = '__all__'