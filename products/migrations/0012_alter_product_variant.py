# Generated by Django 5.0.6 on 2024-06-13 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_productvariant_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], default='None', max_length=10),
        ),
    ]
