from rest_framework import routers
from .api import ProductAPI
from django.urls import path, include

router = routers.DefaultRouter()
router.register('product', ProductAPI, 'Product')

urlpatterns = router.urls