from django.contrib import admin
from .models import *
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username', 'email', 'first_name', 'last_name']
admin.site.register(CustomUser)