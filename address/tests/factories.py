import factory

from orders.tests.factories import OrderFactory
from accounts.tests.factories import UserFactory
from address.models import InstorePickUpPoint, ShippingAddress


class InstorePickUpPointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InstorePickUpPoint
    
    shop_name = 'Jason Moyo'
    country = factory.Iterator(['Nam', 'SA', 'Zim'])


class ShippingAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShippingAddress
    
    pickup_instore = False
    store = factory.SubFactory(InstorePickUpPointFactory)
    customer = factory.SubFactory(UserFactory)
    order = factory.SubFactory(OrderFactory)