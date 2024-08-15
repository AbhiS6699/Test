from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib import messages




def home(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email confirmed
            user.save()
            send_verification_email(request, user)
            messages.success(request, 'Please confirm your email address to complete the registration.')
            return redirect('confirm_email')  # Redirect to confirm email page
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

def send_verification_email(request, user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    message = render_to_string('acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token,
    })
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.content_subtype = "html"  # This is the key line that ensures the email is sent as HTML
    email.send()

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = SetPasswordForm

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

def confirm_email(request):
    return render(request, 'confirm_email.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to your desired page after logout
