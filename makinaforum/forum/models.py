from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="threads")
    public = models.BooleanField(default=False)
    description = models.CharField(max_length=200)
    date = models.DateTimeField('date', auto_now_add=True)
    voters = models.ManyToManyField(User)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="messages")
    message = models.CharField(max_length=200)
    date = models.DateTimeField('date', auto_now_add=True)
