import pytest

from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe

from products.models import Color, Product


def test_currency_str(product_currency):
    assert product_currency.__str__() == "USD"

def test_category_str(product_category):
    assert product_category.__str__() == 'P'

def test_size_str(product_size):
    assert product_size.__str__() == 'Large'

def test_color_str(product_color):
    assert product_color.__str__() == 'black'

def test_color_tag_with_color(product_color):
    result = mark_safe(f'<p style="background-color:{product_color.code}">color</p>')
    assert product_color.color_tag() == result

@pytest.mark.django_db
def test_color_tag_without_color():
    color = Color(name="No Color", code=None)
    assert color.color_tag() == ''

def test_product_str(product):
    assert product.__str__() == 'suit'

@pytest.mark.skip
def test_product_reverse(client, product):
    the_product = product
    url = reverse('products:detail', kwargs={"pk": the_product.id} )
    response = client.get(url)
    assert response.status_code == 200

#@pytest.mark.skip
def test_product_url_image(product):
    assert product.image
    assert product.image.name in product.image.url

def test_product_path(product):
    assert product.image.name.startswith('uploads/product/')

def test_image_tag(product):
    result = mark_safe(f'<img src="{product.image.url}" height="50" />')
    assert product.image_tag() == result 

@pytest.mark.django_db
def test_image_tag_empty():
    p = Product(name='Test', image='')
    assert p.image_tag() == ''

def test_product_variant_str(product_variant):
    assert product_variant.__str__() == product_variant.product.name


