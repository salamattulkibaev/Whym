from django.contrib import admin
from .models import User
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('username', 'phone', 'admin', 'staff', 'active')
    list_filter = ('admin', 'active')
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date', 'email', 'full_address',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'active', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'phone')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)