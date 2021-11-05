from django.db import models

class Event(models.Model):
    Nama=models.CharField(max_length=30)
    Tanggal=models.DateField()
    Waktu=models.TimeField()
    Media=models.CharField(max_length=30)
    Tipe=models.CharField(max_length=50)
    url=models.URLField(max_length = 200)
    Deskripsi=models.TextField()
    Card_Image=models.ImageField(null=True,blank=True, upload_to='images/event')
    Page_Image=models.ImageField(null=True,blank=True, upload_to='images/event')
    created = models.DateTimeField(auto_now_add=True)
