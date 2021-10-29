from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminDateWidget


class EventForm(forms.ModelForm):
    class Meta:
        #Mengambil model Friend
        model=Event
        #Melist semua fields yang perlu diisi
        fields = [
            'Nama',
            'Tanggal',
            'Waktu',
            'Media',
            'Tipe',
            'Deskripsi',
            'Card_Image',
            'Page_Image'
        ]
        widgets={
            'Tanggal':forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'}),
            'Waktu':forms.TimeInput(attrs={'type': 'time'})
        }
        