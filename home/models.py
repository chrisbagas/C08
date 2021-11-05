from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
    message = models.TextField()

    NILAI = (
        ("0",0),
        ("1",1),
        ("2",2),
        ("3",3),
        ("4",4),
        ("5",5),
    )
    
    rating = models.CharField(
        max_length=100,
        choices=NILAI,
        default=0,
    )    