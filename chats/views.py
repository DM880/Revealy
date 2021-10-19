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


        for chat in chats:
            if chat.room_name == room:
                chat.subscribers.add(request.user)
                chat.save()

                return redirect("chat:base_chats")


@login_required
def room_chat(request, room_name):

    room = room_name.replace(" ", "")
    chats = Room.objects.all()
    state = 0

    for chat in chats:
        if request.user in chat.subscribers.all() and chat.room_name == room_name:
            state = 1

    latest_messages =  SubMessage.objects.all().order_by("-timestamp")

    return render(request, 'room.html', {'room_name': room, 'state': state, 'current_room':room_name, 'last_ten_messages':latest_messages})


