from django.contrib import admin
from .models import Category, Status, Post

class CategoryAdmin (admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name')

    class Meta:
        model = Category

class StatusAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ['name']

    class Meta:
        model = Status

class PostAdmin(admin.ModelAdmin):
    search_fields = ['user', 'title']
    list_display = ['id', 'user', 'title','updated_at', 'status']
    list_filter = ['city']

    class Meta:
        model = Post

admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Post, PostAdmin)