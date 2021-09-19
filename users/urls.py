from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = "user"

urlpatterns = [
                path('', views.login_page, name='Login_page'),
                path('main/', views.main, name='main'),
                path('register/',views.register, name='Register'),
                path('logout/', views.user_logout, name='Logout'),
                path('profile/<username>/', views.main_profile, name="Profile"),
                path('profile/<username>/info/', views.info_profile, name="info_profile"),
                path('delete_post/<post_id>/', views.delete_post, name="delete_post"),
                path('upload_cover/', views.upload_cover, name="upload_cover"),
                path('upload_profile_image/', views.upload_profile_image, name="upload_profile_img"),
                path('password_reset/', views.password_reset, name="password_reset"),

            ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
