from rest_framework import viewsets, permissions
from .models import (
    InvoiceProduct, 
    InvoiceProductItem, 
    ProductBasket, 
    PaymentConfirmation, 
    PaymentMethod,
    PaymentAccount,
)
from .serializers import (
    InvoiceProductItemSerializer, 
    InvoiceProductItemSerializerCreate, 
    InvoiceProductSerializer, 
    InvoiceProductSerializerCreate,
    ProductBasketSerializer, 
    PaymentConfirmationSerializer, 
    ProductBasketSerializerView,
    PaymentMethodSerializer,
    PaymentAccountSerialer
)
from .filters import (
    ProductBasketFilter, 
    InvoiceProdcutItemFilter,
    PaymentAccountFilter
)

class InvoiceProductAPI(viewsets.ModelViewSet):
    serializer_class = InvoiceProductSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    def get_queryset(self, *args, **kwargs):
        queryset = InvoiceProduct.objects.all()
        return queryset
        # user = self.request.user
        # if (user.is_authenticated or user.is_superuser):
        # return

class InvoiceProductCreateAPI(viewsets.ModelViewSet):
    serializer_class = InvoiceProductSerializerCreate
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    def get_queryset(self, *args, **kwargs):
        queryset = InvoiceProduct.objects.all()
        return queryset
        # user = self.request.user
        # if (user.is_authenticated or user.is_superuser):
        # return

class InvoiceProductItemAPI(viewsets.ModelViewSet):
    serializer_class = InvoiceProductItemSerializer
    filterset_class = InvoiceProdcutItemFilter
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    def get_queryset(self, *args, **kwargs):
        queryset = InvoiceProductItem.objects.all()
        return queryset
    
class InvoiceProductItemCreateAPI(viewsets.ModelViewSet):
    serializer_class = InvoiceProductItemSerializerCreate
    filterset_class = InvoiceProdcutItemFilter
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    def get_queryset(self, *args, **kwargs):
        queryset = InvoiceProductItem.objects.all()
        return queryset


class ProductBasketAPI(viewsets.ModelViewSet):
    serializer_class = ProductBasketSerializer
    filterset_class = ProductBasketFilter
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if (user.is_authenticated or user.is_superuser):
            queryset = ProductBasket.objects.filter(user=user, is_checked_out=False)
            return queryset
        return

class ProductBasketListAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductBasketSerializerView
    filterset_class = ProductBasketFilter
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if (user.is_authenticated or user.is_superuser):
            queryset = ProductBasket.objects.filter(user=user, is_checked_out=False)
            return queryset
        return

class PaymentConfirmationAPI(viewsets.ModelViewSet):
    serializer_class = PaymentConfirmationSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = PaymentConfirmation.objects.all()
        return queryset
        # if (user.is_authenticated or user.is_superuser):
        # return


class PaymentMethodAPI(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()

class PaymentAccountAPI(viewsets.ModelViewSet):
    serializer_class = PaymentAccountSerialer
    filterset_class = PaymentAccountFilter
    queryset = PaymentAccount.objects.all()

