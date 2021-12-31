from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def vote_requirement(self, user):
        # Check if user already voted
        user_votes = user.vote_set.all()
        if user_votes.filter(survey=self).exists():
            return False
        return True

    def get_survey_count(self):
        return self.vote_set.count()

    def natural_key(self):
        return self.creator

    def __str__(self):
        return self.title


class Option(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=75)

    def get_option_count(self):
        return self.vote_set.count()

    def __str__(self):
        return self.text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
