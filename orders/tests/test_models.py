import pytest
import uuid


def test_order_str(user_order):
    assert str(user_order) == '14'

def test_generate_transaction_id(user_order):
    assert user_order.generate_transaction_id() is not None

def test_order_save_method(user_order):
    user_order.transaction_id = None
    user_order.save()

    assert user_order.transaction_id is not None
    assert isinstance(user_order.transaction_id, str)

def test_get_cart_total(user_order, user_order_item):
    assert user_order.get_cart_total == user_order_item.product.price * user_order_item.quantity

def test_get_cart_items(user_order, user_order_item):
    assert user_order.get_cart_items == user_order_item.quantity

def test_order_item_str(user_order_item):
    assert str(user_order_item) == user_order_item.product.name

def test_get_total(user_order_item):
    assert user_order_item.get_total == 4.00

def test_product_variant_size(user_order_item):
    assert user_order_item.product_variant_size == "Large"

def test_product_variant_color(user_order_item):
    assert user_order_item.product_variant_color == "black"

