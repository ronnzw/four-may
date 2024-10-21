import factory

from currencies.models import Currency
from django.core.files.base import ContentFile
from faker import Faker


from products.models import Category, Size, Color, Product, ProductVariant


fake = Faker()

class CurrencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency
    
    code = 'USD'
    name = 'United States Dollars'
    symbol = '$'
    factor = 1.0
    is_active = True
    is_base = True
    is_default = True

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'P'

class SizeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Size
    
    name = 'Large'

class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color
    
    name = 'black'
    code = '#ffffff'

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'suit'
    price = 2.00
    variant = 'Size'
    
    @factory.lazy_attribute
    def image(self):
        return ContentFile(
            b'some_image_content', 'test_image.jpg'
        )

class ProductVariantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductVariant

    product = factory.SubFactory(ProductFactory)
    color = factory.SubFactory(ColorFactory)
    size = factory.SubFactory(SizeFactory)  