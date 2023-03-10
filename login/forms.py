from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username"
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'})
    )

    password2 = forms.CharField(
        label="Confirm password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
