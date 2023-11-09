from django.core.mail import send_mail
import random
from django.conf import settings
from .models import CustomUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=CustomUser)
def sent_email_via_otp(sender, instance, created, **kwargs):
    if created:
        subject = 'Your account varification email'
        otp = random.randint(1000, 9999)
        message = f'Your otp is {otp}'
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [instance.email], fail_silently=True)
        user = CustomUser.objects.get(email = instance.email)
        user.otp = otp
        user.save()
