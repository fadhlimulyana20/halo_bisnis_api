from rest_framework import viewsets
from .serializers import (
    ServiceTypeSerializer
)

from .models import (
    ServiceType
)

class ServiceTypeAPI(viewsets.ModelViewSet):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.filter(is_active = True)
