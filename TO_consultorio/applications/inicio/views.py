from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse

@login_required
def startpage(request):
    return render(request,'inicio/startpage.html' )

def logout_view(request):
    logout(request)
    return redirect('login')