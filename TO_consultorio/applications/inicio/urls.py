from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('inicio/',views.startpage, name='startpage'),
    # path('contact/',views.contact, name='contact')
]