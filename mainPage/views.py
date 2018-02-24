from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'mainPage/index.html', locals())

def entrance(request):
    return render(request, 'mainPage/pages/entrance.html', locals())

def signup(request):
    return render(request, 'mainPage/pages/register.html', locals())