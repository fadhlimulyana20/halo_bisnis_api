from rest_framework import routers
from .api import (
    ProjectAPI,
    ProjectDetailAPI
)

router = routers.DefaultRouter()

router.register('project', ProjectAPI, 'project')
router.register('project_detail', ProjectDetailAPI, 'project_detail')


urlpatterns = router.urls