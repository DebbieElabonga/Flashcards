from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','contact']
from .models import Card



class CardForm(forms.ModelForm):
    class Meta:
        model=Card
        fields=['title','subject','note']
