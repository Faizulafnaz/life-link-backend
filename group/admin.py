from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Groups)
admin.site.register(Channel)
admin.site.register(VideoChannel)
admin.site.register(VoiceChannel)
admin.site.register(GroupMember)
admin.site.register(GroupMessage)