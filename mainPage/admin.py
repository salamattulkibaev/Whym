from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import  *

# Register your models here.
class RegionAdmin (admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ['name']

    class Meta:
        model = Region

class CityAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', 'region']
    list_display = ('id', 'name', 'region')
    list_filter = ('region',)

    class Meta:
        model = City

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

class RecallAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'created_at']
    search_fields = ['user', 'text']
    list_filter = ['user']

    class Meta:
        model = Recall

class MessageAdmin(admin.ModelAdmin):
    search_fields = ['to_user','from_user', 'text']
    list_display = ['id', 'to_user','from_user', 'text']
    list_filter = ['to_user','from_user']

    class Meta:
        model = Message

class PostAdmin(admin.ModelAdmin):
    search_fields = ['user', 'title']
    list_display = ['id', 'user', 'title','updated_at', 'status']
    list_filter = ['city']

    class Meta:
        model = Post


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['author']
    list_display = ['id', 'text', 'author', 'to_post', 'created_at']
    list_filter = ['author', 'to_post']

    class Meta:
        model = Comment

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'phone', 'admin', 'staff', 'active')
    list_filter = ('admin', 'active')
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date', 'email', 'full_address',)}),
        ('Permissions', {'fields': ('admin', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'phone')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Recall, RecallAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)