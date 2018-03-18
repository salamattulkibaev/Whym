from django.shortcuts import render, get_object_or_404
from mainPage.models import User
from .forms import PostForm
from mainPage.models import Post

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'addPost/add-post.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(User, id = id)
    context = {
        'instance': instance,
    }
    return render(request, 'addPost/post_detail.html', context)

def post_update(request, id=None):

    instance = get_object_or_404(User, id=id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'instance': instance,
        'form': form,
    }
    return render(request, 'addPost/add-post.html', context)