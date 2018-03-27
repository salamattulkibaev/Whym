from django.contrib import admin
from .models import User
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ( 'phone', 'first_name', 'admin', 'staff', 'active')
    list_filter = ('admin', 'active')
    fieldsets = (
        (None, {'fields': ( 'phone','first_name', 'password')}),
        ('Дополнительные данные', {'fields': ('last_name', 'birth_date', 'email', 'full_address',)}),
        ('Разрешения', {'fields': ('admin', 'staff', 'active', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'first_name', 'password1', 'password2')}
        ),
    )
    search_fields = ['phone', 'first_name']
    ordering = ['first_name',]
    filter_horizontal = []

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)