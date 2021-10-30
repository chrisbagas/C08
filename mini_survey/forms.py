from django import forms
from .models import Survey


class CreateSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            'title',
            'description',
            'first_option',
            'second_option',
            'third_option',
        ]
