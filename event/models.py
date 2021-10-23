from django.db import models

class Event(models.Model):
    Nama=models.CharField(max_length=30)
    Tanggal=models.DateTimeField()
    Media=models.CharField(max_length=30)
    Sinopsis=models.TextField(default="")
    Deskripsi=models.TextField()
    Card_Image=models.ImageField(null=True,blank=True, upload_to='images/')
