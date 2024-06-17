# Generated by Django 4.0 on 2024-06-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color_index', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='products.Color'),
        ),
    ]
