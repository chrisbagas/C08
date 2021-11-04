from django import forms
from .models import Option, Survey


class CreateSurveyForm(forms.ModelForm):
    option1 = forms.CharField(label='Option 1', max_length=75,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    option2 = forms.CharField(label='Option 2', max_length=75,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Survey
        fields = [
            'title',
            'description',
            'option1',
            'option2'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 20}),
        }


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
