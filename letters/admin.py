from django.contrib import admin
from .models import Letter

class LetterAdmin(admin.ModelAdmin):
    search_fields = ['to_user','from_user', 'text']
    list_display = ['id', 'to_user','from_user', 'text']
    list_filter = ['to_user','from_user']

    class Meta:
        model = Letter

admin.site.register(Letter, LetterAdmin)