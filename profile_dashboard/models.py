from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='images/profile_dashboard')

    def __str__(self):
        return f'{self.user.username} Profile'
