from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import DiaryPage


class AddPageForm(forms.ModelForm):
    class Meta:
        model = DiaryPage
        fields = "__all__"
        exclude = ["customer"]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]
