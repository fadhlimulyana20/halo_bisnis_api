# Generated by Django 3.0.7 on 2020-06-28 01:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0022_auto_20200626_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceproductitem',
            name='grand_total',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoiceproduct',
            name='due_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 1, 8, 3, 118854, tzinfo=utc)),
        ),
    ]