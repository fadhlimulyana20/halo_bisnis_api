# Generated by Django 3.0.7 on 2020-06-15 13:48

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.product_directory_path),
        ),
    ]
