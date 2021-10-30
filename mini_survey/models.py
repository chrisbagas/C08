from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    first_option = models.CharField(max_length=50)
    second_option = models.CharField(max_length=50)
    third_option = models.CharField(max_length=50)
    first_option_count = models.IntegerField(default=0)
    second_option_count = models.IntegerField(default=0)
    third_option_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
