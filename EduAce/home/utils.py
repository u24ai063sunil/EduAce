# utils.py
import random
from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(email, otp, purpose="Verification"):
    send_mail(
        subject=f"EduAce {purpose} Code",
        message=f"Your 6-digit verification code is: {otp}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
