from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    avatar = models.ImageField(upload_to="friendship/uploads/")
    passions = models.ManyToManyField('Passion', related_name="passions", blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    friends = models.ManyToManyField('self', blank=True)


    @property
    def briefBio(self):
        bioList = self.bio.split(" ")
        return " ".join(bioList[0:10]) + "..."

    def serialize(self):
        return {
            "avatar": self.avatar,
            "username": self.username,
            "email": self.email,
            "bio": self.bio,
            "briefBio": self.briefBio,
            "passions": map(lambda passion: {"name": passion.name, "id": passion.id}, self.passions.all()), 
        }


class Passion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Request(models.Model):
    sender = models.ForeignKey(User, related_name="sentRequests", on_delete=models.CASCADE)
    to = models.ForeignKey(User, related_name="receivedRequests", on_delete=models.CASCADE)