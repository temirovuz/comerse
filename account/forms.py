from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User