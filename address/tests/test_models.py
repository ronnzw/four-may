import pytest


def test_instore_pickup_str(instore_pickup):
    assert str(instore_pickup) == 'Jason Moyo'

def test_shipping_address_str(shipping_address):
    assert str(shipping_address) == f'Delivery address for: {shipping_address.customer}'
