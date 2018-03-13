from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import  *

# Register your models here.
class RegionAdmin (admin.ModelAdmin):
    # list_display = ["id", "name"]
    search_fields = ['id', 'name']

    class Meta:
        model = Region

class CityAdmin(admin.ModelAdmin):
    # list_display = ["id", "name"]
    search_fields = ['id', 'name', 'region']

    class Meta:
        model = City

class CategoryAdmin (admin.ModelAdmin):
    search_fields = ['id', 'name']

    class Meta:
        model = Category

class StatusAdmin(admin.ModelAdmin):
    # list_display = ["id", "name"]
    search_fields = ['id', 'name']

    class Meta:
        model = Status


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'phone', 'admin', 'staff', 'active')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date', 'email', 'full_address', )}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'phone', 'email', 'first_name', 'last_name')
    ordering = ('username', 'phone',)
    filter_horizontal = ()


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)