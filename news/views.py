from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from django.contrib.auth.decorators import login_required
from users.models import *

# Create your views here.

def news_feed(request):

    posts = UserPost.objects.all().order_by('-publish')


    return render(request, "news_feed.html", {'posts': posts})
