from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.CharField(null=True, blank=True, default="", max_length= 200)
    image = models.ImageField(null=True, blank=True, upload_to='images/profile_dashboard')

    def __str__(self):
        return f'{self.user.username} Profile'
