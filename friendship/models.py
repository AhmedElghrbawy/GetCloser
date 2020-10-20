from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    avatar = models.ImageField(upload_to="friendship/uploads/")
    passions = models.ManyToManyField('Passion', related_name="passions", blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    friends = models.ManyToManyField('self', blank=True)


class Passion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Request(models.Model):
    sender = models.ForeignKey(User, related_name="sentRequests", on_delete=models.CASCADE)
    to = models.ForeignKey(User, related_name="receivedRequests", on_delete=models.CASCADE)