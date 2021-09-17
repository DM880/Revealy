from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    specific_chat = models.CharField(max_length=100)

    def __str__(self):
        return self.specific_chat


class Room(models.Model):
    subscribers = models.ManyToManyField(User, blank=True)
    room_name = models.CharField(max_length=100)
    specific_room_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "{room_chat}/{room_name}".format(room_chat=self.specific_room_chat,room_name=self.room_name)

class SubMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)