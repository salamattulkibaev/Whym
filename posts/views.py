from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import PostForm
from .models import Post
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from django.contrib import messages
from comments.forms import CommentForm

def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if not request.user.is_authenticated:
        msg1 = "Для добавления объявлений"
        msg2 = "зарегистрируйтесь"
        msg3 = "войдите на сайт"
        return render(request, 'posts/add-post.html', {'msg': {"msg1": msg1, "msg2": msg2, "msg3": msg3}})

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
    return render(request, 'posts/add-post.html', context)

def post_detail(request, slug=None):
    admin = False
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_admin:
            admin = True
    instance = get_object_or_404(Post, slug = slug)
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id,
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('text')
        new_comment, created = Comment.objects.get_or_create(
                            author = request.user,
                            content_type = content_type,
                            object_id = obj_id,
                            text = content_data,)
        if created:
            print("It's ok!")
    comments = instance.comments #Comment.objects.filter_by_instance(instance=instance)
    context = {
        'instance': instance,
        'admin': admin,
        'comments': comments,
        'comment_form': form,
    }
    return render(request, 'posts/post_detail.html', context)

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
    return render(request, 'posts/add-post.html', context)

def post_delete(request, slug = None):
    if not request.user.is_staff or not request.user.is_admin:
        raise Http404
    instance = get_object_or_404(Post, slug = slug)
    instance.delete()
    messages.success(request, "Успешно удалено!")
    return redirect('/')
