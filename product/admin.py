from django.contrib import admin
from .models import Product, ProductType, ProductCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductCategory)