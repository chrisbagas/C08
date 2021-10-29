from django.db import models

class Event(models.Model):
    Nama=models.CharField(max_length=30)
    Tanggal=models.DateField()
    Waktu=models.TimeField()
    Media=models.CharField(max_length=30)
    Tipe=models.CharField(max_length=50)
    Deskripsi=models.TextField()
    Card_Image=models.ImageField(null=True,blank=True, upload_to='images/event')
    Page_Image=models.ImageField(null=True,blank=True, upload_to='images/event')
