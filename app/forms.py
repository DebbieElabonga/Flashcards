from django import forms
from .models import Card
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CardForm(forms.ModelForm):
    class Meta:
        model=Card
        fields=['title','subject','note']

class UserCreationFormm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
