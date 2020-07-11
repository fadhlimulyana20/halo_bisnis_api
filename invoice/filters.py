from django_filters import rest_framework as filters
from .models import (
    ProductBasket, 
    InvoiceProductItem,
    PaymentAccount,
)

class ProductBasketFilter(filters.FilterSet):
    class Meta:
        model = ProductBasket
        fields = ['product']

class InvoiceProdcutItemFilter(filters.FilterSet):
    class Meta:
        model = InvoiceProductItem
        fields = ['invoice']

class PaymentAccountFilter(filters.FilterSet):
    class Meta:
        model = PaymentAccount
        fields = ['method']