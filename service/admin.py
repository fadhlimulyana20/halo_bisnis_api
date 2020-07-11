from django.contrib import admin
from .models import ServiceType, Technology

# Register your models here.
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_display_links = ['name']

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'initial_price']
    list_display_links = ['name']

admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Technology, TechnologyAdmin)
