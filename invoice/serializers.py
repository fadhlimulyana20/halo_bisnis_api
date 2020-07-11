from rest_framework import serializers
from .models import (
    InvoiceProduct, 
    ProductBasket, 
    PaymentConfirmation, 
    InvoiceProductItem, 
    PaymentAccount, 
    PaymentMethod,
)
from product.serializers import ProductSerializer
from user_area.serializers import UserSerializer

class InvoiceProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = InvoiceProductItem
        fields = '__all__'

class InvoiceProductItemSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = InvoiceProductItem
        fields = '__all__'

class InvoiceProductCreate(serializers.ModelSerializer):
    class Meta:
        model = InvoiceProductItem
        fields = '__all__'

class InvoiceProductSerializer(serializers.ModelSerializer):
    # total_bills = serializers.SerializerMethodField
    # # is_due = serializers.SerializerMethodField
    # item = InvoiceProductItemSerializer()
    user = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y")
    due_at = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = InvoiceProduct
        fields = [
            'id',
            '__str__',
            'user',
            'created_at',
            'due_at',
            'is_paid',
            'item',
            'is_due',
            'payment',
            'total_bills'
        ]

class InvoiceProductSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = InvoiceProduct
        fields = [
            'id',
            '__str__',
            'user',
            'created_at',
            'due_at',
            'is_paid',
            'item',
            'is_due',
            'payment',
            'total_bills'
        ]


class ProductBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBasket
        fields = [
            'id',
            'product',
            'amount',
            'user',
            'created_at',
            'is_checked_out',
        ]

        
    def create(self, validated_data):
        product_basket, created = ProductBasket.objects.update_or_create(
            product = validated_data['product'],
            user = validated_data['user'],
            is_checked_out = False,
            defaults = {
                'amount' : validated_data['amount']
            }
        )

        return product_basket

class ProductBasketSerializerView(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductBasket
        fields = [
            'id',
            'product',
            'amount',
            'user',
            'created_at',
            'is_checked_out',
        ]

class PaymentConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentConfirmation
        fields = [
            'id',
            'method',
            'provider_from',
            'payment_from',
            'name_from',
            'payment_to',
            'invoiceproduct'
        ]
    
    def create(self, validated_data):
        confirm = PaymentConfirmation(
            method = validated_data['method'],
            provider_from = validated_data['provider_from'],
            payment_from = validated_data['payment_from'],
            name_from = validated_data['name_from'],
            payment_to = validated_data['payment_to']
        )
        confirm.save()
        confirm.invoiceproduct = validated_data['invoiceproduct']
        return confirm


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class PaymentAccountSerialer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAccount
        fields = [
            '__str__',
            'id',
            'provider',
            'name',
            'account_number',
            'description',
            'method'
        ]
        