# Generated migration to create Google OAuth SocialApp on first deploy

from django.db import migrations
from django.contrib.sites.models import Site
import os

def create_google_app(apps, schema_editor):
    """Create Google OAuth SocialApp if it doesn't exist."""
    SocialApp = apps.get_model('socialaccount', 'SocialApp')
    
    # Check if Google app already exists
    if SocialApp.objects.filter(provider='google').exists():
        return
    
    # Get or create the Site
    site, _ = Site.objects.get_or_create(
        pk=1,
        defaults={'domain': 'example.com', 'name': 'EduAce'}
    )
    
    # Create Google SocialApp
    google_app = SocialApp.objects.create(
        provider='google',
        name='Google',
        client_id=os.environ.get('GOOGLE_OAUTH_CLIENT_ID', ''),
        secret=os.environ.get('GOOGLE_OAUTH_SECRET', ''),
    )
    google_app.sites.add(site)

def reverse_google_app(apps, schema_editor):
    """Remove Google SocialApp on migration rollback."""
    SocialApp = apps.get_model('socialaccount', 'SocialApp')
    SocialApp.objects.filter(provider='google').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('socialaccount', '0004_app_provider_id_settings'),
        ('home', '0010_remove_email_verification'),
    ]

    operations = [
        migrations.RunPython(create_google_app, reverse_google_app),
    ]
