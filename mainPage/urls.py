from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name = 'home'),
    path('entrance', views.entrance, name="entrance"),
    path('signup', views.signup, name="register"),

]
