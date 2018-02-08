from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.welcome, name = ''),
    path('entrance', views.entrance, name='entrance')
]
