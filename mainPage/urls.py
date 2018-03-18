from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('accounts/login', views.entrance, name="login"),
    path('accounts/register',views.register, name="register"),
    # path('entrance', views.LoginView.as_view(), name="entrance"),
    # path('signup', views.RegisterView.as_view(), name="register"),
]
