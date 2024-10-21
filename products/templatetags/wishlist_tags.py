from django import template
from django.contrib.auth.models import User
from products.models import Product

register = template.Library()

@register.filter
def in_wishlist(user, product):
    return user.wishlist_set.filter(product=product).exists()