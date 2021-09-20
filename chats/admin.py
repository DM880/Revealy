from django.contrib import admin
from .models import *

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ('room_name', 'specific_room_chat')
    # search_fields = ['room_name', 'specific_room_chat','subscribers']


ChatModels = [Chat, SubMessage]


admin.site.register(ChatModels)
admin.site.register(Room, RoomAdmin)