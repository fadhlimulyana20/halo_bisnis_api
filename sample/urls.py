from rest_framework import routers
from .api import ProductSampleAPI

router = routers.DefaultRouter()

router.register('product_sample', ProductSampleAPI, 'product_sample')

urlpatterns = router.urls
