from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = "news"

urlpatterns = [
                path('', views.news_feed, name="news_feed"),

    ]