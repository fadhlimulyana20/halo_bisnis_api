from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    type__name = filters.CharFilter(field_name='type', lookup_expr='name')
    category__name = filters.CharFilter(field_name='category', lookup_expr='name')

    class Meta:
        model = Product
        fields = ['category', 'type']