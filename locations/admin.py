from django.contrib import admin
from .models import Region, City

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

admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)