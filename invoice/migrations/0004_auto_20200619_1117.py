# Generated by Django 3.0.7 on 2020-06-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoiceproduct_due_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceproduct',
            name='due_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
