from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    participant_first_name = models.CharField(max_length=30)
    participant_last_name = models.CharField(max_length=30)
    participant_email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return f'{self.participant_first_name} {self.participant_last_name}'
