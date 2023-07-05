from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import logout
from django.urls import reverse

def startpage(request):
    return render(request,'inicio/startpage.html' )


