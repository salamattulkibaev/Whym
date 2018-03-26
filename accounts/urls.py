from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('accounts/login', views.LoginView.as_view(), name="login"),
    path('accounts/register',views.RegisterView.as_view(), name="register"),
    path('accounts/logout', views.logout_view, name="logout"),
    # path('accounts/register',views.login_view, name="register"),
    # path('accounts/login', views.login_view, name="login"),
]
