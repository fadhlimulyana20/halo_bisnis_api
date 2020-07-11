from rest_framework import routers
from .api import (
    InvoiceProductAPI, 
    InvoiceProductCreateAPI,
    ProductBasketAPI, 
    PaymentConfirmationAPI, 
    ProductBasketListAPI, 
    InvoiceProductItemAPI,
    InvoiceProductItemCreateAPI, 
    PaymentMethodAPI,
    PaymentAccountAPI
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register('invoice_product', InvoiceProductAPI, 'InvoiceProduct')
router.register('invoice_product_create', InvoiceProductCreateAPI, 'InvoiceProductCreate')
router.register('invoice_product_item', InvoiceProductItemAPI, 'InvoiceProductItem')
router.register('invoice_product_item_create', InvoiceProductItemCreateAPI, 'InvoiceProductItemCreate')
router.register('product_basket', ProductBasketAPI, 'ProductBasket')
router.register('product_basket_list', ProductBasketListAPI, 'ProductBasketList')
router.register('payment_confirmation', PaymentConfirmationAPI, 'PaymentConfirmation')
router.register('payment_method', PaymentMethodAPI, 'PaymentMethod')
router.register('payment_account', PaymentAccountAPI, 'PaymentAccount')

# urlpatterns = [
#     path('product_basket', ProductBasketAPI.as_view())
# ]


urlpatterns = router.urls