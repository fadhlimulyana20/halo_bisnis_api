from django.contrib import admin
from .models import InvoiceProductItem, InvoiceProduct, ProductBasket, PaymentAccount, PaymentMethod, PaymentConfirmation

# Register your models here.
class InvoiceProductItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'invoice', 'total', 'discount', 'grand_total']
    # list_display_links = ['id']


class InvoiceProductInline(admin.TabularInline):
    model = InvoiceProductItem

class InvoiceProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    inlines = [InvoiceProductInline,]
    list_display = ['__str__', 'user','created_at', 'is_due', 'is_paid', 'total_bills']
    list_filter = ['created_at','due_at', 'is_paid', 'user']

class ProductBasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'amount', 'created_at', 'is_checked_out']
    list_display_links = ['id', 'product']

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name']

class PaymentAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'method', 'provider', 'name', 'account_number']
    list_display_links = ['id', 'method', 'provider']

class PaymentConfirmationAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_to', 'name_from', 'payment_from', 'provider_from', 'method', 'invoiceproduct']


admin.site.register(InvoiceProductItem, InvoiceProductItemAdmin)
admin.site.register(InvoiceProduct, InvoiceProductAdmin)
admin.site.register(ProductBasket, ProductBasketAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(PaymentAccount, PaymentAccountAdmin)
admin.site.register(PaymentConfirmation, PaymentConfirmationAdmin)
