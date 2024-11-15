# Generated by Django 5.0.6 on 2024-06-13 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem'),
        ('products', '0011_alter_productvariant_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productvariant'),
        ),
    ]
