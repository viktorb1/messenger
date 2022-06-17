from django.db import models
from django.contrib.auth.models import AbstractUser

class Conversation(models.Model):
    conversation_name = models.CharField(max_length=50)
    time_created = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    conversations = models.ManyToManyField(Conversation)

class Message(models.Model):
    text = models.CharField(max_length=200)
    time_sent = models.DateTimeField(auto_now_add=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text