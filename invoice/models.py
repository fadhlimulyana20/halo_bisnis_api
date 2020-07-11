from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

# Create your models here.
class InvoiceProductItem(models.Model):
    invoice = models.ForeignKey(to='InvoiceProduct', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=0, max_digits=10, default=1)
    discount = models.FloatField(default=0)
    total = models.DecimalField(decimal_places=0, max_digits=10, default=0)
    grand_total = models.DecimalField(decimal_places=0, max_digits=10, default=0)

    def save(self, *args, **kwargs):
        self.total = self.amount * self.product.price
        new_total = (float(self.total)*float(1 - self.discount))
        self.grand_total =  int(new_total)
        super().save(*args, **kwargs) 

class InvoiceProduct(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=2))
    is_paid = models.BooleanField(default=False)
    payment = models.OneToOneField(to='PaymentConfirmation', on_delete=models.CASCADE, null=True, blank=True)
    item = models.ManyToManyField(Product, through=InvoiceProductItem)

    def __str__(self):
        invoice_number = "INV/P/{}/{}".format(self.created_at.date(), self.id)
        return invoice_number
  
    def is_due(self):
        due_date = self.due_at
        if (due_date < timezone.now()):
            return True
        return False 
    
    def total_bills(self):
        # item= InvoiceProductItem.objects.all()
        # total = Product.objects.filter(product_ivoice = self.invoice_item) .aggregate(Sum('price'))
        total = 0
        item = self.item.all()
        for obj in item:
            product_item = obj.invoiceproductitem_set.filter(invoice = self.id)
            for product in product_item:
                total += product.grand_total
        # if (item):
        #     return item[0]
        return total

class ProductBasket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=0, max_digits=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_checked_out = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.created_at = timezone.now()
        super().save(*args, **kwargs) 

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class PaymentAccount(models.Model):
    method = models.ForeignKey(to=PaymentMethod, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return '{} - {}'.format(self.provider, self.account_number)

class PaymentConfirmation(models.Model):
    method = models.ForeignKey(to=PaymentMethod, on_delete=models.CASCADE)
    provider_from = models.CharField(max_length=50)
    name_from = models.CharField(max_length=100)
    payment_from = models.CharField(max_length=50)
    payment_to = models.ForeignKey(to=PaymentAccount, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.payment_to, self.id)
    
    # def get_invoice(self, *args, **kwargs):




