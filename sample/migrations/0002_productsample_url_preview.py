# Generated by Django 3.0.7 on 2020-07-10 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsample',
            name='url_preview',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]