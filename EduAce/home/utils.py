# # utils.py
# import random
# from django.core.mail import send_mail
# from django.conf import settings

# def send_otp_email(email, otp, purpose="Verification"):
#     send_mail(
#         subject=f"EduAce {purpose} Code",
#         message=f"Your 6-digit verification code is: {otp}",
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[email],
#         fail_silently=False,
#     )
# utils.py
# utils.py
import requests
from django.conf import settings

def send_otp_email(email, otp, purpose="Verification"):
    url = "https://api.resend.com/emails"

    headers = {
        "Authorization": f"Bearer {settings.RESEND_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "from": "EduAce <onboarding@resend.dev>",
        "to": [email],
        "subject": f"EduAce {purpose} Code",
        "html": f"""
        <h2>Your EduAce Verification Code</h2>
        <h1>{otp}</h1>
        <p>This OTP is valid for 5 minutes.</p>
        """
    }

    try:
        requests.post(url, json=data, headers=headers, timeout=5)
    except Exception as e:
        print("EMAIL ERROR:", e)
