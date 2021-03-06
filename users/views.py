from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from .forms import *
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
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from chats.models import *
from chats.templates import *
from chats.views import *
from chats.urls import *
import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from django.conf import settings


# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('chat:base_chats')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('chat:base_chats'))
        else:
            return render(request, 'users/login_page.html', {'error': True})
    else:
        return render(request, 'users/login_page.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('user:Login_page')


@csrf_protect
def register(request):
    if request.user.is_authenticated:
        return redirect('chat:base_chats')

    elif request.method == "POST":

        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()

        return redirect('user:Login_page')

    else:
        return render(request, 'users/register.html')


@receiver(post_save, sender=User)
def create_user_profile_info(sender, instance, created, **kwargs):
    if created:
        ProfileInfo.objects.create(user=instance)


def password_reset(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':request.META['HTTP_HOST'],
					'site_name': 'Revealy',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					message= Mail(
					    from_email=settings.EMAIL_HOST,
					    to_emails=user.email,
					    subject=subject,
					    html_content=email
					    )

					try:
					    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
					    response = sg.send(message)
					    print(response)
					except Exception as e:
					    print(e)


					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("user:Login_page")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request, "password_reset/password_reset.html", context={"password_reset_form":password_reset_form})


@login_required
def delete_user(request, username):

    if request.method == "POST":

        form = DeleteUserForm(request.POST)

        if form.is_valid():

            choice = form.cleaned_data.get('response')

            if choice == "yes":

                user = User.objects.get(username = username)
                user.delete()

                return redirect("user:Login_page")

            else:

                return redirect("user:Profile", username)

    form = DeleteUserForm()

    return render(request, "users/delete_user.html", {"username":username, 'form': form})


# POST & IMAGES UPLOAD

# django cleanup for deletion of previous image if new uploaded

@login_required
def upload_cover(request):
    user = ProfileInfo.objects.get(user = request.user)

    if request.method == "POST":
        form = UploadCoverForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            user = form.save(False)

            cover = form.cleaned_data.get("cover_image")
            if cover:
                image = Image.open(cover)
                image_data = BytesIO()
                image.save(fp=image_data, format=image.format)
                image_file = ImageFile(image_data)
                user.cover_image.save('{}.cover.{}'.format(user,image.format), image_file)
            user.save()
            return redirect("user:Profile", request.user.username)
    else:
        form = UploadCoverForm(instance=user)

    return render(request, "uploads/upload_cover.html",{"form": form})



@login_required
def upload_profile_image(request):
    user = ProfileInfo.objects.get(user = request.user)

    if request.method == "POST":
        form = UploadProfileImgForm(request.POST, request.FILES or None, instance=user)

        if form.is_valid():
            user = form.save(False)

            img = form.cleaned_data.get("profile_image")
            if img:
                image = Image.open(img)
                image_data = BytesIO()
                image.save(fp=image_data, format=image.format)
                image_file = ImageFile(image_data)
                user.profile_image.save('{}.profile_image.{}'.format(user,image.format), image_file)#img.name
            user.save()
            return redirect("user:Profile", request.user.username)
    else:
        form = UploadProfileImgForm(instance=user)

    return render(request, "uploads/upload_profile_img.html",{"form": form})


#Create Post
@login_required
def main_profile(request, username):

    username =  request.user.username.title()
    user_post = ProfileInfo.objects.get(user = request.user)

    queryset = UserPost.objects.all().filter(user = user_post)

    posts = []

    for query in queryset:
        posts.append(query)

    if request.method == 'POST':

        post = request.POST.get('post')
        new_post = UserPost.objects.create(user=user_post,posts=post)

        return redirect('user:Profile',username)

    return render(request, 'users/base.html', {"username" : username, "posts" : posts, "user_post": user_post})


@login_required
def delete_post(request, post_id):

    username =  request.user.username

    post = UserPost.objects.all().filter(posts = post_id)

    post.delete()

    return redirect("user:Profile", username)



# Main Profile sections

@login_required
def info_profile(request, username):

    queryset = Room.objects.all().filter(subscribers = request.user)

    rooms = []

    for query in queryset:
        rooms.append(query.room_name)

    user_post = ProfileInfo.objects.get(user = request.user)

    return render(request, "users/info.html", {'user_post': user_post, 'rooms':rooms})


@login_required
def reveals(request,username):

    all_users = User.objects.all()

    user_post = ProfileInfo.objects.get(user = request.user)

    return render(request, "users/reveals.html", {"user_post":user_post, "all_users":all_users})
