from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    total_games = models.IntegerField(default=0)
    win_games =models.IntegerField(default=0)

class  Game(models.Model):
    name = models.CharField(max_length=50)
    single_player = models.BooleanField(default=True)
    multiplayer = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "single_player": self.single_player,
            "multiplayer": self.multiplayer,
        }
