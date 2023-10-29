from django.core.mail import send_mail
import random
from django.conf import settings
from .models import CustomUser


def sent_email_via_otp(email):
    subject = 'Your account varification email'
    otp = random.randint(1000, 9999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email], fail_silently=True)
    user = CustomUser.objects.get(email = email)
    user.otp = otp
    user.save()
