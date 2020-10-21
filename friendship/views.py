from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def index(request):
    return render(request, "friendship/index.html", {
        "users": map(lambda user: user.serialize(request.user), User.objects.all())
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "friendship/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "friendship/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        bio = request.POST["bio"]
        avatar = request.FILES['avatar']
        passionIds = request.POST.getlist('passion')
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "friendship/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.bio = bio
            user.avatar = avatar
            for passionId in passionIds:
                passionId = int(passionId)
                user.passions.add(Passion.objects.get(id=passionId)) 
            user.save()
        except IntegrityError:
            return render(request, "friendship/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        passions = Passion.objects.all()
        return render(request, "friendship/register.html", {
            "passions": passions
        })