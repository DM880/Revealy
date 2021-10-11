from django.contrib import admin
from django.urls import path, re_path
from .views import *
from django.conf.urls import url


app_name = "chat"

urlpatterns=[
              path('', base_chats, name="base_chats"),
              path('<room>/sub/', sub_or_unsub, name="sub_or_unsub"),
              path('<str:room_name>/', room_chat, name='room_chat'),
    ]