from django import forms
from django.contrib.auth.models import User
from django.forms.fields import ImageField
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']