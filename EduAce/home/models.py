from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    subjects = models.TextField()
    contact = models.CharField(max_length=15)

    is_email_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, blank=True, null=True)
    
    def __str__(self):
        return self.user.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
#model for expense
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    category = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - ₹{self.amount}" 

#for studyplan
class StudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_plans')
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    day = models.CharField(max_length=10)
    total_hours = models.IntegerField()
    subjects = models.TextField()
    priority_subject = models.CharField(max_length=100)
    break_duration = models.IntegerField()
    plan_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"   