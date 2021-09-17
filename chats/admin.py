from django.contrib import admin
from .models import *

# Register your models here.

ChatModels = [Chat, Room, SubMessage]


admin.site.register(ChatModels)