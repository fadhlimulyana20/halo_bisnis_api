# Generated by Django 3.0.7 on 2020-06-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200615_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.CharField(default='1.0.0', max_length=20),
        ),
    ]
