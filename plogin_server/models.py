from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(User)
    captain = models.ForeignKey(User,
                                related_name='captain_user',
                                on_delete=models.CASCADE, default=1)


class Contest(models.Model):
    name = models.CharField(max_length=255)
    sport_type = models.CharField(default='plogging',
                                  max_length=500)
    team_max_size = models.IntegerField(default=10)
    teams = models.ManyToManyField(Team)
    start_timestamp = models.IntegerField(default=0)
    end_timestamp = models.IntegerField(default=0)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE,
                               related_name='winner_team',
                               null=True)


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, default=1)
    collected = models.FloatField(default=0.0)
