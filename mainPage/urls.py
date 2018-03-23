from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    # path('accounts/login', views.login_view, name="login"),
    path('accounts/login', views.LoginView.as_view(), name="login"), #
    # path('accounts/register',views.login_view, name="register"),
    path('accounts/register',views.RegisterView.as_view(), name="register"),#.
    path('accounts/logout', views.logout_view, name="logout"),

]
