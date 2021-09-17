from django.contrib import admin
from .models import *


# Register your models here.

class PostsInLine(admin.StackedInline):
    model = UserPost


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
            PostsInLine,
        ]

admin.site.register(ProfileInfo , ProfileAdmin)
