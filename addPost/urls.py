from . import views
from django.urls import path, include

urlpatterns = [
    path('addPost', views.add_post, name="addPost"),
    path('<int:id>/', views.post_detail, name="detail"),
    path('<int:id>/edit', views.post_update, name="update"),
]
