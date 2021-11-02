from django import forms
from .models import Option, Survey


class CreateSurveyForm(forms.ModelForm):
    option1 = forms.CharField(label='Option 1', max_length=75)
    option2 = forms.CharField(label='Option 2', max_length=75)

    class Meta:
        model = Survey
        fields = [
            'title',
            'description',
            'option1',
            'option2'
        ]


class EditSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            'title',
            'description',
        ]


class AddOptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = [
            'text',
        ]
