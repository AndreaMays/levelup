from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    description = models.CharField(max_length=50)
    number_of_people = models.CharField(max_length=50)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="Attending")