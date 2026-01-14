from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests

from .forms import ContactForm, UserRegistrationForm, LoginForm,StudyPlanForm
from .models import Profile,StudyPlan
#API
import requests
from django.conf import settings

def query_openrouter_model(user_message):
    OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",

        "HTTP-Referer": "http://127.0.0.1:8003/",  # Required by OpenRouter
        # "X-Title": "home",           # Your app name (optional)
    }
    
    payload = {
        "model": "meta-llama/llama-3-70b-instruct",
        "messages": [{"role": "user", "content": user_message}],
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise error for bad status codes
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("DeepSeek API Error:", e)
        return "⚠️ Sorry, the AI is currently unavailable. Please try again later."
    
@login_required
def ai_homework_helper(request):
    chat_history = request.session.get('chat_history', [])

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'clear_chat':
            request.session['chat_history'] = []
            return redirect('ai_homework_helper')

        elif action == 'get_solution':
            user_message = request.POST.get('question', '').strip()
            
            if user_message:
                chat_history.append({"role": "user", "content": user_message})
                bot_reply = query_openrouter_model(user_message)
                chat_history.append({"role": "assistant", "content": bot_reply})
                request.session['chat_history'] = chat_history

    latest_response = chat_history[-1]["content"] if chat_history else "✨ Your AI-generated solution will appear here."

    return render(request, 'ai_homework_helper.html', {
        'latest_response': latest_response,
        'chat_history': chat_history,
    })

# Main Pages
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for reaching out! We will get back to you soon.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')  

def features(request):
    return render(request, 'features.html') 

def resources(request):
    return render(request, 'resources.html')

@login_required
def calender(request):
    return render(request, 'calender.html')

def focustimer(request):
    return render(request, 'focustimer.html')

def expensetracker(request):
    return render(request, 'expensetracker.html')

# views.py
import random
from .utils import send_otp_email

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            full_name = form.cleaned_data['full_name']

            # 1️⃣ Create user (inactive until email verified)
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name,
                is_active=False
            )

            # 2️⃣ Create / update profile
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.college = form.cleaned_data['college']
            profile.degree = form.cleaned_data['degree']
            profile.year = form.cleaned_data['year']
            profile.subjects = form.cleaned_data['subjects']
            profile.contact = form.cleaned_data['contact']

            # 3️⃣ Generate OTP
            otp = str(random.randint(100000, 999999))
            profile.email_otp = otp
            profile.is_email_verified = False
            profile.save()

            # 4️⃣ Send OTP email
            send_otp_email(email, otp)

            # 5️⃣ Store user id in session for verification
            request.session['verify_user_id'] = user.id

            messages.success(
                request,
                "Account created! A 6-digit verification code has been sent to your email."
            )

            return redirect('verify_email')

    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})

def verify_email(request):
    user_id = request.session.get('verify_user_id')
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        otp = request.POST.get('otp')

        if otp == user.profile.email_otp:
            user.is_active = True
            user.save()
            user.profile.is_email_verified = True
            user.profile.email_otp = ""
            user.profile.save()

            messages.success(request, "Email verified successfully!")
            return redirect('login')
        else:
            messages.error(request, "Invalid verification code")

    return render(request, 'verify_email.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.profile.is_email_verified:
                    messages.error(request, "Please verify your email first.")
                    return redirect('login')
                login(request, user)
                return redirect('features')  # Redirect after login
            else:
                messages.error(request, "Invalid email or password. Please check your credentials.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})


@login_required   #after adding expense tracker
def profile(request):
    user = request.user
    try:
        profile = user.profile
        expenses = Expense.objects.filter(user=user).order_by('-date_added')
        expenses_count = expenses.count()
        expenses_total = sum(expense.amount for expense in expenses)
        latest_expense = expenses.first()
    except Exception as e:
        profile = None
        expenses = []
        expenses_count = 0
        expenses_total = 0
        latest_expense = None
        
    context = {
        'user': user,
        'profile': profile,
        'expenses': expenses,
        'expenses_count': expenses_count,
        'expenses_total': expenses_total,
        'latest_expense': latest_expense
    }
    return render(request, 'profile.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

#for expense tracker
import json
from .models import Expense

# Add this to your existing views.py file
@login_required
def save_expenses(request):
    if request.method == 'POST':
        expenses_data = request.POST.get('expenses_data')
        if expenses_data:
            try:
                data = json.loads(expenses_data)
                for expense in data['expenses']:
                    Expense.objects.create(
                        user=request.user,
                        name=expense['name'],
                        amount=expense['amount'],
                        category=expense['category']
                    )
                messages.success(request, "Expenses saved successfully!")
            except Exception as e:
                messages.error(request, f"Error saving expenses: {str(e)}")
        else:
            messages.error(request, "No expenses data provided")
    
    return redirect('expensetracker')

@login_required
def clear_expenses(request):
    if request.method == 'POST':
        Expense.objects.filter(user=request.user).delete()
        messages.success(request, "All expenses have been cleared.")
    return redirect('profile')

#for studyplan
# Add to views.py
@login_required
def study_planner(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'generate':
            form = StudyPlanForm(request.POST)
            if form.is_valid():
                # Generate the study plan
                hours = form.cleaned_data['available_hours']
                subjects = [s.strip() for s in form.cleaned_data['subjects'].split(',')]
                priority = form.cleaned_data['priority']
                break_time = form.cleaned_data['breaks']
                date = form.cleaned_data['date']
                day = form.cleaned_data['day']
                
                # Calculate time allocation
                high_priority_weight = 1.5
                total_weight = sum(high_priority_weight if sub == priority else 1 for sub in subjects)
                
                plan_details = []
                for subject in subjects:
                    weight = high_priority_weight if subject == priority else 1
                    time = (weight / total_weight) * hours
                    plan_details.append(f"{subject}: {time:.1f} hours")
                
                context = {
                    'form': form,
                    'generated_plan': {
                        'date': date,
                        'day': day,
                        'subjects': subjects,
                        'priority': priority,
                        'break_time': break_time,
                        'total_hours': hours,
                        'plan_details': plan_details,
                    }
                }
                return render(request, 'studyplanner.html', context)
        
        elif action == 'save':
            # Save the generated plan
            date = request.POST.get('date')
            day = request.POST.get('day')
            hours = request.POST.get('available_hours')
            subjects = request.POST.get('subjects')
            priority = request.POST.get('priority')
            breaks = request.POST.get('breaks')
            plan_details = request.POST.get('plan_details')
            
            if all([date, day, hours, subjects, priority, breaks, plan_details]):
                StudyPlan.objects.create(
                    user=request.user,
                    title=f"Study Plan for {day}, {date}",
                    date=date,
                    day=day,
                    total_hours=hours,
                    subjects=subjects,
                    priority_subject=priority,
                    break_duration=breaks,
                    plan_details=plan_details
                )
                messages.success(request, "Study plan saved successfully!")
                return redirect('studyplanner')
    
    # Handle delete request
    elif request.method == 'GET' and 'delete' in request.GET:
        plan_id = request.GET.get('delete')
        try:
            plan = StudyPlan.objects.get(id=plan_id, user=request.user)
            plan.delete()
            messages.success(request, "Study plan deleted successfully!")
        except StudyPlan.DoesNotExist:
            messages.error(request, "Plan not found or you don't have permission to delete it.")
        return redirect('studyplanner')
    
    form = StudyPlanForm()
    saved_plans = StudyPlan.objects.filter(user=request.user).order_by('-date')
    return render(request, 'studyplanner.html', {
        'form': form,
        'saved_plans': saved_plans
    })