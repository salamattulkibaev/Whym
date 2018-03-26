from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import PostForm
from mainPage.models import Post
from django.contrib import messages

def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if not request.user.is_authenticated:
        msg =  "Сначало войдите в аккаунт!"
        return render(request, 'addPost/add-post.html', {'msg': msg})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # messages.success(request, "Объявление добавлено успешно!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        pass
        # messages.error(request, "Объяление не добавлено!")
    context = {
        "form": form,
    }
    return render(request, 'addPost/add-post.html', context)

def post_detail(request, slug=None):
    admin = False
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_admin:
            admin = True
    instance = get_object_or_404(Post, slug = slug)
    context = {
        'instance': instance,
        'admin': admin
    }
    return render(request, 'addPost/post_detail.html', context)

def post_update(request, slug = None):
    if not request.user.is_staff or not request.user.is_admin:
        raise Http404
    instance = get_object_or_404(Post, slug = slug)
    form = PostForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Объявление обновлено!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Не обновлено!")
    context = {
        'instance': instance,
        'form': form,
    }
    return render(request, 'addPost/add-post.html', context)

def post_delete(request, slug = None):
    if not request.user.is_staff or not request.user.is_admin:
        raise Http404
    instance = get_object_or_404(Post, slug = slug)
    instance.delete()
    messages.success(request, "Успешно удалено!")
    return redirect('/')
