from django.db import models

class Event(models.Model):
    Nama=models.CharField(max_length=30)
    Date=models.DateTimeField()
    Media=models.CharField(max_length=30)
    Deskripsi=models.TextField()
