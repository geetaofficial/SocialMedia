from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(forms.ModelForm):
    """User Login Form"""
    class Meta:
        model = CustomUser
        fields = '__all__'

class SignupForm(UserCreationForm):
    """User sign-up Form"""
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    keep_signin = forms.BooleanField(initial=True,required=False)