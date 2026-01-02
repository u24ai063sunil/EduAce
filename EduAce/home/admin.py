from django.contrib import admin

# Register your models here.
#for contact form 
from .models import ContactMessage

admin.site.register(ContactMessage)
#for admin 
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)