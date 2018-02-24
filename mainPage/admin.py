from django.contrib import admin
from django.contrib.auth.models import User
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


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)