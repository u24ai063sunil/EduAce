# Generated migration to create Google OAuth SocialApp on first deploy

from django.db import migrations
import os

def create_google_app(apps, schema_editor):
    """Create Google OAuth SocialApp if it doesn't exist."""
    SocialApp = apps.get_model('socialaccount', 'SocialApp')
    Site = apps.get_model('sites', 'Site')
    
    # Check if Google app already exists
    if SocialApp.objects.filter(provider='google').exists():
        return
    
    # Get the default site (pk=1 should exist from sites migration)
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        # If default site doesn't exist, create it
        site = Site.objects.create(pk=1, domain='example.com', name='EduAce')
    
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
        ('sites', '0002_alter_domain_unique'),
        ('socialaccount', '0004_app_provider_id_settings'),
        ('home', '0010_remove_email_verification'),
    ]

    operations = [
        migrations.RunPython(create_google_app, reverse_google_app),
    ]
