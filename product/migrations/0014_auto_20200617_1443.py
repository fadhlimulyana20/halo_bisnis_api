# Generated by Django 3.0.7 on 2020-06-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20200617_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='framework',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='deskripso produk', max_length=30000),
        ),
    ]
