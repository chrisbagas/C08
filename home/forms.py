from django import forms
from django.forms import fields, widgets
from .models import FeedbackModel

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['message','rating']

        widgets = {
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Feedback'
                }
            ),

            'rating': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }