from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('sign_up/',views.sign_up,name="sign-up"),
    path('change_password', views.change_password, name='change_password'),
]