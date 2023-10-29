from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_varified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, blank=True, null=True)
    
    def __str__(self):
        return self.username
