from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account


# فورم تسجيل مستخدم جديد
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ["username", "phone", "address", "password1", "password2"]


# فورم تسجيل دخول
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ["username", "password"]
