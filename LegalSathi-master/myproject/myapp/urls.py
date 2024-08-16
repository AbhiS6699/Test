# myapp/urls.py

from django.urls import path
from . import views
from .views import signup_view, login_view, activate
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='landing_page'), 
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'), # Define the home view
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('confirm-email/', views.confirm_email, name='confirm_email'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.logout_view, name='logout'),
    path('service-request/', views.service_request, name='service_request'),
    path('submit-form/', views.form_submission_view, name='form_submission'),





]
