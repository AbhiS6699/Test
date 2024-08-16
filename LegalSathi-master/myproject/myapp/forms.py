from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email
    
class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'remember_me')

class ServiceRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact = forms.CharField(max_length=15)
    related = forms.ChoiceField(choices=[
        ('family', 'Family Law'),
        ('criminal', 'Criminal Law'),
        ('corporate', 'Corporate Law'),
        ('other', 'Other')
    ])