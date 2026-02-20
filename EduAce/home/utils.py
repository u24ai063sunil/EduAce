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
import logging
import requests
from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_otp_email(email, otp, purpose="Verification"):
    """Send OTP via Resend API if available, otherwise fall back to SMTP.

    Returns True on success, False on failure.
    """
    # Try Resend API when API key is configured
    api_key = getattr(settings, "RESEND_API_KEY", None)
    if api_key:
        url = "https://api.resend.com/emails"

        headers = {
            "Authorization": f"Bearer {api_key}",
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
            """,
        }

        try:
            resp = requests.post(url, json=data, headers=headers, timeout=getattr(settings, "EMAIL_TIMEOUT", 5))
            if resp.status_code in (200, 201, 202):
                return True
            logger.error("Resend API error sending email to %s: %s %s", email, resp.status_code, resp.text)
        except Exception:
            logger.exception("Exception while sending email via Resend to %s", email)

    # Fallback to Django SMTP
    email_host_user = getattr(settings, "EMAIL_HOST_USER", None)
    email_host_password = getattr(settings, "EMAIL_HOST_PASSWORD", None)
    if email_host_user and email_host_password:
        subject = f"EduAce {purpose} Code"
        message = f"Your 6-digit verification code is: {otp}"
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", email_host_user)
        try:
            send_mail(subject, message, from_email, [email], fail_silently=False)
            return True
        except Exception:
            logger.exception("Exception while sending email via SMTP to %s", email)

    logger.error("No email backend available or sending failed for %s", email)
    return False
