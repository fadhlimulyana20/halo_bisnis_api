from django.db import models

# Create your models here.
class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=None)
    is_active = models.BooleanField(default=True)

    def __str__(self, *args, **kwargs):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=None)
    initial_price = models.DecimalField(decimal_places=0, max_digits=10)

    def __str__(self, *args, **kwargs):
        return self.name