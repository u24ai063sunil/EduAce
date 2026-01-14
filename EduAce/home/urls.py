from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('signup/', views.signup, name='signup'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("reset-password/", views.reset_password, name="reset_password"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('features/resources/', views.resources, name='resources'),
    path('features/studyplanner/', views.study_planner, name='studyplanner'),
    path('features/ai-helper/', views.ai_homework_helper, name='ai_homework_helper'),
    path('features/calender/',views.calender, name='calender'),
    path('features/focustimer/',views.focustimer, name='focustimer'),
    path('features/expensetracker/',views.expensetracker, name='expensetracker'),
    # Add this to your urlpatterns list
    path('features/expensetracker/save/', views.save_expenses, name='save_expenses'),
    path('profile/clear-expenses/', views.clear_expenses, name='clear_expenses'),
]