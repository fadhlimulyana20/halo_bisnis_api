from rest_framework import viewsets, permissions
from .serializers import ProductSampleSerializer
from .models import ProductSample

class ProductSampleAPI(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.isA
    # ]

    serializer_class = ProductSampleSerializer
    queryset = ProductSample.objects.all()