import pytest
from pytest_factoryboy import register
from allauth.socialaccount.models import SocialLogin
from allauth.socialaccount.signals import social_account_added

from products.tests.factories import (
    CategoryFactory,SizeFactory, ColorFactory, ProductFactory, CurrencyFactory, ProductVariantFactory
    )
from accounts.tests.factories import (CustomerFactory, UserFactory, EmailAddressFactory
)
from orders.tests.factories import OrderFactory, OrderItemFactory
from address.tests.factories import InstorePickUpPointFactory, ShippingAddressFactory


register(CategoryFactory)
register(SizeFactory)
register(ColorFactory)
register(ProductFactory)
register(CurrencyFactory)
register(ProductVariantFactory)
register(CustomerFactory)
register(UserFactory)
register(EmailAddressFactory)
register(OrderFactory)
register(OrderItemFactory)
register(InstorePickUpPointFactory)
register(ShippingAddressFactory)


@pytest.fixture
def product_currency(db, currency_factory):
    curr = currency_factory.create()
    return curr

@pytest.fixture
def product_category(db, category_factory):
    category = category_factory.create()
    return category

@pytest.fixture
def product_size(db, size_factory):
    size = size_factory.create()
    return size

@pytest.fixture
def product_color(db, color_factory):
    color = color_factory.create()
    return color

@pytest.fixture
def product(db, product_factory):
    product_item = product_factory.create()
    return product_item

@pytest.fixture
def product_variant(db, product_variant_factory):
    v = product_variant_factory()
    return v

# accounts
@pytest.fixture
def customer(db, customer_factory):
    cust = customer_factory()
    return cust 

@pytest.fixture
def user_with_email(db, user_factory, email_address_factory):
    user = user_factory()
    email_address = email_address_factory(user=user, verified=False)
    return user, email_address

@pytest.fixture
def sociallogin(db, user_with_email):
    user, _ = user_with_email
    return SocialLogin(user=user)

@pytest.fixture
def user(db,user_factory):
    return user_factory()

@pytest.fixture
def user_order(db, order_factory, user):
    order = order_factory(customer=user)
    return order

@pytest.fixture
def user_order_item(db, order_item_factory, user_order):
    order_it = order_item_factory(order=user_order)
    return order_it

@pytest.fixture
def instore_pickup(db, instore_pick_up_point_factory):
    return instore_pick_up_point_factory()

@pytest.fixture
def shipping_address(db, shipping_address_factory, user, instore_pickup,user_order):
    ship_add = shipping_address_factory(store=instore_pickup,customer=user, order=user_order)
    return ship_add