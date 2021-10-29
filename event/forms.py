from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        #Mengambil model Friend
        model=Event
        #Melist semua fields yang perlu diisi
        fields = [
            'Nama',
            'Tanggal',
            'Media',
            'Sinopsis',
            'Deskripsi',
            'Card_Image',
            'Page_Image'
        ]