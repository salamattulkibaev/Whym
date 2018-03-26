from django.contrib import admin
from .models import Message
class MessageAdmin(admin.ModelAdmin):
    search_fields = ['to_user','from_user', 'text']
    list_display = ['id', 'to_user','from_user', 'text']
    list_filter = ['to_user','from_user']

    class Meta:
        model = Message

admin.site.register(Message, MessageAdmin)
