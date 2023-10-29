from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='groups')


class Channel(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    is_admin_only = models.BooleanField(default=False)

class VideoChannel(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    is_admin_only = models.BooleanField(default=False)


class GroupMember(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_lefted = models.BooleanField(default=False)
    is_ban = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

class GroupMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    send_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['send_at']
