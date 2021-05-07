from django.db.models.aggregates import Max
from levelupapi.models.game_type import GameType
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_game = models.ForeignKey(GameType, on_delete=models.CASCADE)
    name_of_game = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)
    how_many_players = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)