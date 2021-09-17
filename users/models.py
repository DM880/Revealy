from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime


# Create your models here.

class ProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    cover_image = models.ImageField(null=True, blank=True,upload_to='cover/')
    profile_image = models.ImageField(null=True, blank=True,upload_to='avatar/')
    # info = models.CharField(max_length=50, blank=True)
    # groups = models.OneToManyField()
    # rewards = model.CharField()
    # reveals = model.OneToManyField()
    # slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.user.username

class UserPost(models.Model):
    user = models.ForeignKey(ProfileInfo, related_name="posts", on_delete=models.CASCADE)
    posts = models.TextField(max_length = 500, unique=False)
    publish = models.DateTimeField(blank=True, null=True,default=datetime.datetime.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.posts[:5]

#  unique=True, blank=True, default=uuid.uuid4

