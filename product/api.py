from rest_framework import generics,permissions, viewsets

from .serializers import ProductSerializer
from .models import Product, ProductCategory, ProductCategory
from .filters import ProductFilter

class ProductAPI(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(active = True)
    filterset_class = ProductFilter

    # def get_object(self):
    #     queryset = Product.objects.all()
    #     return queryset

