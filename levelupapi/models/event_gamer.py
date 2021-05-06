from levelupapi.models.event import Event
from django.db import models
from django.db.models.deletion import CASCADE

class EventGamer(models.Model):
    Event = models.ForeignKey("Event", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)