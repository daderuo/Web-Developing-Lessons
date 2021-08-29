from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import *
from .form import *


def index(request):
    auctions = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html",{
        "auctions": auctions
    })

@login_required(login_url='/login/')
def create(request):

    form = CreateListingForm()

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        start_price = request.POST['start_price']
        #img_url = request.FILES
        #img_url = request.POST['img']
        category = request.POST['category']

        #return HttpResponse(img_url)
    
        listing = Listing(
            title = title,
            description = description,
            start_price = start_price, 
            current_price = start_price, 
            final_price = start_price, 
            image = request.FILES['image'],
            category = category,
            active = True,
            creator = request.user
            )

        
        #img_url = Listing(image = request.FILES['img'])
        #img_url.save()
        listing.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        "form" : form
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.POST["next"]
        user = authenticate(request, username=username, password=password)


        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(next))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password.",
                "next": next
            })
    else:
        next = request.GET.get('next', '/index/')
        next = next[1:]
        next = next[:-1]
        if next == "":
            next = 'index'
        return render(request, "auctions/login.html",{
            "next": next
        })


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


def auctions(request, id):
    auction = Listing.objects.get(id=id)


    watchlist = False
    bid = False

    
    return render(request, "auctions/auction.html",{
        "auction": auction,
        "watchlist": watchlist,
        "bid": bid
    })