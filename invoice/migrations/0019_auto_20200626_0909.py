# Generated by Django 3.0.7 on 2020-06-26 02:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200617_1443'),
        ('invoice', '0018_auto_20200626_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceporductitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AlterField(
            model_name='invoiceproduct',
            name='due_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 2, 9, 3, 831500, tzinfo=utc)),
        ),
    ]
