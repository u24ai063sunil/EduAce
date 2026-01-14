from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import ContactMessage, Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['college', 'degree', 'year', 'subjects', 'contact']

# For contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

# For user registration
class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    college = forms.CharField(max_length=100, required=False)
    degree = forms.CharField(max_length=100, required=False)
    year = forms.ChoiceField(choices=[
        ('', 'Select Year'),
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year')
    ], required=False)
    subjects = forms.CharField(max_length=255, required=False)
    contact = forms.CharField(max_length=15, required=False)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Use Django's built-in password validation
        validate_password(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        
        return cleaned_data

# Login form
class LoginForm(forms.Form):
    username = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

#studyplan form
class StudyPlanForm(forms.Form):
    date = forms.DateField(required=True)
    day = forms.ChoiceField(choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ], required=True)
    available_hours = forms.IntegerField(min_value=1, max_value=16, required=True)
    subjects = forms.CharField(max_length=255, required=True)
    priority = forms.CharField(max_length=100, required=True)
    breaks = forms.IntegerField(min_value=5, max_value=60, required=True)

