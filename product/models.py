from django.db import models
from django.utils import timezone

# Create your models here.

def product_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'product/product_{0}/{1}'.format(self.id, filename)

class Product(models.Model):
    name = models.CharField(max_length=100, default="nama produk")
    price = models.DecimalField(decimal_places=0, max_digits=10)
    description = models.TextField(max_length=None, default="deskripso produk")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to=product_directory_path, blank=True, null=True)
    type = models.ForeignKey('ProductType', on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField('ProductCategory')
    version = models.CharField(max_length=20, blank=False, null=False, default="1.0.0")
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    framework = models.CharField(max_length=100, blank=True, null=True)
    live_preview = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to=product_directory_path, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs) 

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=300)

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
