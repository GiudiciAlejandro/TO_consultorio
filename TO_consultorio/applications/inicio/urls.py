from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('inicio/',views.startpage, name='startpage'),
    # path('login/',views.login, name='login'),
    # path('logout/',views.logout, name='logout'),
    # path('contact/',views.contact, name='contact')
]