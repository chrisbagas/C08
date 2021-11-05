from django import forms
from .models import Option, Survey


class CreateSurveyForm(forms.ModelForm):
    option1 = forms.CharField(label='Option 1', max_length=75,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 1'}))
    option2 = forms.CharField(label='Option 2', max_length=75,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 2'}))

    class Meta:
        model = Survey
        fields = [
            'title',
            'description',
            'option1',
            'option2'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 20, 'placeholder': 'Description'}),
        }


class EditSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            'title',
            'description',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 20, 'placeholder': 'Description'}),
        }


class AddOptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = [
            'text',
        ]
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option text'})
        }
