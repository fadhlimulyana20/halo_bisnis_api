# Generated by Django 3.0.7 on 2020-06-19 04:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20200619_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceproduct',
            name='due_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 4, 22, 58, 76890, tzinfo=utc)),
        ),
    ]