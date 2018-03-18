from django.shortcuts import render, redirect
from mainPage.models import *
from django.views.generic import CreateView, FormView
from mainPage.forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect, Http404 ,HttpResponse
from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login ,get_user_model

def welcome(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'mainPage/index.html', context)

def entrance(request):
    if request.method != 'POST':
        return render(request, 'mainPage/pages/login.html')
    else:
        pass


def register(request):
    if request.method is not 'POST':
        return render(request, 'mainPage/pages/register.html')
    else:
        pass
