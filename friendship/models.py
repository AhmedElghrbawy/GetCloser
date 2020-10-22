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

    def getMutualFriends(self, user):
        myFriends = {}
        for friend in self.friends.all():
            myFriends[friend.id] = friend
        
        mutualFriends = []
        
        for friend in user.friends.all():
            if friend.id in myFriends:
                mutualFriends.append(friend)
        return mutualFriends


    def serialize(self, requestUser):
        mutualFriends = self.getMutualFriends(requestUser)
        return {
            "id": self.id,
            "avatar": self.avatar,
            "username": self.username,
            "email": self.email,
            "bio": self.bio,
            "briefBio": self.briefBio,
            "passions": map(lambda passion: {"name": passion.name, "id": passion.id}, self.passions.all()),
            "isFriend": self.friends.filter(id=requestUser.id).exists(),
            "receivedRequest": Request.objects.filter(to=self, sender=requestUser).exists(), # self received request from request.user
            "sentRequest": Request.objects.filter(to=requestUser, sender=self).exists(), # self sent request to request.user
            "mutualFriends": mutualFriends,
            "numMutualFriends": len(mutualFriends)
        }
    

    @property
    def numRequests(self):
        '''
        number of friend requests sent to self
        '''
        return Request.objects.filter(to=self).count()


class Passion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Request(models.Model):
    sender = models.ForeignKey(User, related_name="sentRequests", on_delete=models.CASCADE)
    to = models.ForeignKey(User, related_name="receivedRequests", on_delete=models.CASCADE)

    def __str__(self):
        return f"from {self.sender} to {self.to}"
