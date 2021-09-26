from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile
from datetime import datetime

# Create your views here.

@login_required
def base_chats(request):

    all_chats = Room.objects.all()

    return render(request, "chats_base.html", {'all_chats':all_chats})

@login_required
def specific_room(request, room):

    return render(request, "specific_room.html", {'room':room})

@login_required
def sub_or_unsub(request, room):

    if request.method == "POST":

        user_chats = Room.objects.all().filter(subscribers = request.user)
        chats = Room.objects.all()

        if user_chats.count() > 0:

            for user_chat in user_chats:

                if user_chat.room_name == room:
                    user_chat.subscribers.remove(request.user)
                    user_chat.save()

                    return redirect("chat:base_chats")

                else:
                    for chat in chats:
                        if chat.room_name == room:
                            chat.subscribers.add(request.user)
                            chat.save()

                            return redirect("chat:base_chats")
        else:
            for chat in chats:
                if chat.room_name == room:
                    chat.subscribers.add(request.user)
                    chat.save()

                    return redirect("chat:base_chats")



