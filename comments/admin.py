from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['author']
    list_display = ['id', 'text', 'author', 'created_at']
    list_filter = ['author',]

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)