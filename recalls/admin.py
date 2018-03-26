from django.contrib import admin
from .models import Recall

class RecallAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'created_at']
    search_fields = ['user', 'text']
    list_filter = ['user']

    class Meta:
        model = Recall

admin.site.register(Recall, RecallAdmin)
