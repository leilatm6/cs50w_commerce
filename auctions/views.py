from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Products, Category
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def index(request):
    return render(request, "auctions/index.html")


@login_required
def createlisting(request):
    if request.method == "POST":
        title = request.POST["title"]
        price = request.POST["price"]
        description = request.POST["description"]
        imageurl = request.POST["imageurl"]
        try:
            category = Category.objects.get(pk=request.POST["category"])
        except ObjectDoesNotExist:
            category = None
        print(category)
        newproduct = Products(title=title, initialprice=price, description=description, datetime=timezone.now(),
                              category=category, imageurl=imageurl, creatoruser=request.user)
        newproduct.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/createlisting.html", {
        'category': Category.objects.all()
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
