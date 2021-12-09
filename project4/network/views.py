from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .form import *
from datetime import datetime,timezone
from django.core import serializers
import json
from django.core.paginator import Paginator



def index(request):

    NewPost = CreatePostForm()

    if request.user.is_authenticated:            

        if request.method == "POST":
            text = request.POST['text']
        
            post = Post(
                text = text,
                date_time = datetime.now(timezone.utc),
                author = request.user, 
                )               
            post.save()

            return HttpResponseRedirect(reverse("index"))
    

    return render(request, "network/index.html", {
        "NewPost":NewPost
    })


def update(request):
    a = request.GET.get('a')
    t = request.GET.get('t')
    d = datetime.fromisoformat(request.GET.get('d'))
    l = int(request.GET.get('l'))
    new_t = request.GET.get('new_t')
    new_l = int(request.GET.get('new_l'))

    liked = False

    user = User.objects.get(username = a)
    post = Post.objects.get(author=user,text=t)

    if t == new_t:
        pass
    else:
        post.text = new_t

    if l == new_l:
        pass
    else:
        #post.like = new_l
        if new_l < l:
            for like in post.like.all():
                if user == like:
                    post.like.remove(request.user)
            liked = False
        else:
            post.like.add(request.user)
            liked = True
    #post.date_time = datetime.now(timezone.utc)
    post.save()

    Json = {
            "text": post.text,
            "date": post.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "author": f"{post.author.username}",
            "like": post.like.count(),
            "liked": liked
        }

    return JsonResponse({
        "post":Json
    })

def posts(request):
    #start = int(request.GET.get("start") or 0)
    #end = int(request.GET.get("end") or (start+9))
    
    page = int(request.GET.get("page") or 1)
    profile = request.GET.get("profile") or "" 
    f = request.GET.get("f") or False   

    if profile == "":
        if f:
            if request.user.is_authenticated:
                a=[]
                authors = Net.objects.filter(follower = request.user)
                for author in authors:
                    a.append(author.followed)
                posts = Post.objects.filter(author__in = a)#[start:end] 
            else:
                a = []
                p = {
                    "text": "Log in please",
                    "date": "As soon as possible",
                    "author": "",
                    "like": 1000,
                    "liked":True,
                }
                a.append(p)
                return JsonResponse({
                    "post":a,
                    "next_button":False,
                    "previous_button":False,
                    "user": request.user.username
                })
        else:
            posts = Post.objects.all()#[start:end] 
    else:
        aut = User.objects.get(username = profile)
        posts = Post.objects.filter(author=aut.id) 

    
    
    Json = []
    actual =request.user
    for post in posts:
        liked = False
        for u_like in post.like.all():

            if actual == u_like:
                liked =True
            else:
                pass
                
        p = {
            "text": post.text,
            "date": post.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "author": f"{post.author.username}",
            "like": post.like.count(),
            "liked":liked
        }
        
        Json.append(p)
    
    p = Paginator(Json,10)

    return JsonResponse({
        "post":p.page(page).object_list,
        "next_button":p.page(page).has_next(),
        "previous_button":p.page(page).has_previous(),
        "user": request.user.username
    })
    

def profile(request,user):

    u = User.objects.get(username=user)  

    return render(request, "network/profile.html", {
        "u":u,
    })

def remove_follow(request):
    profile = request.GET.get("profile") or ""
    u = User.objects.get(username = profile)
    actual_user = request.user
    f = Net.objects.get(followed=u, follower=actual_user)
    f.delete()

    return JsonResponse({
        "Done":True
    })

def add_follow(request):
    profile = request.GET.get("profile") or ""
    u = User.objects.get(username = profile)
    actual_user = request.user
    f = Net(followed=u, follower=actual_user)
    f.save()

    return JsonResponse({
        "Done":True
    })

def follow(request):
    profile = request.GET.get("profile") or ""

    u = User.objects.get(username = profile)
    actual_user = request.user.username
    already = False
    myself = True

    f = []

    followers = Net.objects.filter(followed=u)
    followeds = Net.objects.filter(follower=u)    

    if u.username == actual_user:
        myself = False

    for follower in followers:

        f = follower.follower.username
        
        if follower.follower.username == actual_user :
            already = True

    Json = {
            "follower": followers.count(),
            "followed": followeds.count(),
            "already": already,
            "logged": request.user.is_authenticated,
            "myself": myself,
            "f":f             
        }

    return JsonResponse({
        "follow":Json
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



