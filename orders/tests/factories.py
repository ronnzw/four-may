import factory
import uuid

from faker import Faker

from orders.models import Order, OrderItem
from accounts.tests.factories import UserFactory
from products.tests.factories import ProductFactory, ProductVariantFactory


fake = Faker()

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(UserFactory)
    transaction_id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    id = '14'

class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    product_variant = factory.SubFactory(ProductVariantFactory)
    quantity = 2
