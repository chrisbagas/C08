from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s | %s | %s | %s' % (self.title, self.author, self.time_created, self.time_modified)


# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=CASCADE)
#     body = models.TextField()