from django.contrib import admin
from .models import ProductSample

# Register your models here.
class ProductSampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service_type', 'technology', 'is_active']
    list_display_links = ['name']

admin.site.register(ProductSample, ProductSampleAdmin)