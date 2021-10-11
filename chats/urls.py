from django.contrib import admin
from django.urls import path, re_path
from .views import *
from django.conf.urls import url


app_name = "chat"

urlpatterns=[
              path('', base_chats, name="base_chats"),
            #   path('<room>/', specific_room, name="specific_room"),
              path('<room>/sub/', sub_or_unsub, name="sub_or_unsub"),
              path('chat/', index, name="index"),
              path('chat/<str:room_name>/', room_chat, name='room_chat'),
    ]