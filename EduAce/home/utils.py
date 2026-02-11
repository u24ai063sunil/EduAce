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
import threading
from django.core.mail import send_mail
from django.conf import settings


def _send(email, otp, purpose):
    """
    Actual email sending function (runs in background thread)
    """
    try:
        send_mail(
            subject=f"EduAce {purpose} Code",
            message=f"Your 6-digit verification code is: {otp}\n\n"
                    f"This OTP is valid for 5 minutes.\n"
                    f"If you did not request this, please ignore.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=True,   # VERY important in production
        )
    except Exception as e:
        print("EMAIL ERROR:", e)   # shows in Render logs


def send_otp_email(email, otp, purpose="Verification"):
    """
    Non-blocking email sender.
    Starts a background thread so signup request doesn't wait for SMTP.
    """
    email_thread = threading.Thread(
        target=_send,
        args=(email, otp, purpose),
        daemon=True   # auto kills thread if worker stops
    )
    email_thread.start()
