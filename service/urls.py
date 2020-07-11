from rest_framework import routers
from .api import (
    ServiceTypeAPI
)

router = routers.DefaultRouter()

router.register('service_type', ServiceTypeAPI, 'service_type')


urlpatterns = router.urls