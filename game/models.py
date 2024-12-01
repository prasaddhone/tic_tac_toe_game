# game/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    # Add related_name to avoid clash with auth.User
    groups = models.ManyToManyField(
        'auth.Group', related_name='game_user_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='game_user_permissions_set', blank=True
    )
