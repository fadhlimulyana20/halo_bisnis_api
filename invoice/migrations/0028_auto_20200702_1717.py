# Generated by Django 3.0.7 on 2020-07-02 10:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0027_auto_20200702_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceproduct',
            name='due_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 10, 17, 20, 425875, tzinfo=utc)),
        ),
    ]
