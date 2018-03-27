from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from django.views.generic import CreateView, FormView
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect, Http404 ,HttpResponse
from django.db.models import Q
from django.utils.http import is_safe_url
from django.utils import timezone
from django.contrib.auth import authenticate, login , logout, get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def welcome(request):
    posts_list = Post.objects.active()
    admin = False
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_admin:
            posts_list = Post.objects.all()
            admin = True
    query = request.GET.get("q")
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )
    else:
        query = ""
    paginator = Paginator(posts_list, 2)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    posts = paginator.get_page(page)
    context = {
        'post_list': posts,
        'page_request_var': page_request_var,
        'admin': admin,
        'query': query,
    }
    return render(request, 'index.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        phone = form.cleaned_data.get("phone")
        password = form.cleaned_data.get("password")
        user = authenticate(phone = phone, password = password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('/')
    return render(request, 'accounts/login.html', {"form": form, })
def logout_view(request):
    logout(request)
    return render(request, 'index.html', {})

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('submit')
        next_post = request.POST.get('submit')
        redirect_path = next_ or next_post or None
        phone = form.cleaned_data.get("phone")
        password = form.cleaned_data.get("password")
        user = authenticate(request, phone = phone, password = password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        return super(LoginView, self).form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/'