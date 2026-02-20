# Generated migration to remove email verification fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_profile_email_otp_profile_is_email_verified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_otp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_email_verified',
        ),
    ]
