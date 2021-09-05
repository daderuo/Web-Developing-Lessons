from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Max


from .models import *
from .form import *


def index(request):
    auctions = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html",{
        "auctions": auctions,
        "text": "Active Auctions"
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
            active = True
            )
               
        #img_url = Listing(image = request.FILES['img'])
        #img_url.save()
        listing.save()
        listing = Listing.objects.get(title = title)
        user = request.user
        user.auctions.add(listing)
        #listing.creator.add() 

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
            return HttpResponseRedirect(next)
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password.",
                "next": next
            })
    else:
        next = request.GET.get('next', '/index/')
        #if next == "":
            #next = 'index'
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
    creator = auction.creator.get()
    error = ''
    minbid = auction.current_price + 1.0
    user = request.user

    if auction.active == False:
        bids = Bids.objects.filter(auction=auction)                    
        for bid in bids:
            if bid.value == auction.final_price:
                winner = bid.user
    else:
        winner = ''

    if request.method == "POST":
        if request.user.is_authenticated:
            if request.POST.get('add'):                
                user.watchlist.add(auction)

            elif request.POST.get('rem'):                
                user.watchlist.remove(auction)

            elif request.POST.get('comment'):                
                NewComment = Comments(
                    user = user,
                    text = request.POST['text'],
                    auction = auction
                )
                NewComment.save()
            
            elif request.POST.get('close'): 
                if user == creator:               
                    auction.active = False
                    auction.final_price = auction.current_price
                    auction.save()
                    bids = Bids.objects.filter(auction=auction)
                    
                    for bid in bids:
                        if bid.value == auction.final_price:
                            winner = bid.user
                        
                    winner.winner.add(auction)
                    #return HttpResponseRedirect(reverse("index"))

            elif request.POST.get('bid'):
                value = float(request.POST["value"])
                if value:
                    bid = Bids(
                        value = value,
                        auction = auction,
                        user = user
                    )
                    bid.save()
                if value > auction.current_price:
                    auction.current_price = value
                    auction.save()
                else:
                    error='Current price is higher then your bid'

    try:
        if user.watchlist.get(id=auction.id):
            watchlist = True
    except:
        watchlist = False

    try:
        comments = Comments.objects.filter(auction=auction)
    except:
        comments = 'ciao'

    commentForm = NewCommentForm

    form = NewBidForm()
    return render(request, "auctions/auction.html",{
        "auction": auction,
        "creator": creator,
        "form": form,
        "error": error,
        "minbid": minbid,
        "watchlist":watchlist,
        "winner":winner,
        "comments": comments,
        'commentForm': commentForm
    })

def WatchList(request):
    watchlist = request.user.watchlist.all()
    return render(request, "auctions/index.html",{
        "auctions": watchlist,
        "text": "Your watchlist"
    })

def categories(request,selected= None):
    if selected:
        auctions = Listing.objects.filter(category=selected, active=True)
        return render(request, "auctions/index.html",{
            "auctions": auctions,
            "text": "Category " + selected
        })
    
    categorie = []
    for item in cat:
        categorie.append(item[0])
        
    return render(request, "auctions/categories.html",{
        "categories": categorie
    })