import json
from django.shortcuts import render

from .models import Order
from products.models import Product

# Create your views here.
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(   customer=customer, completed=False)
        items = order.cart_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except KeyError:
            cart = {}

        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

        for i in cart:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_items'] += cart[i]['quantity']
            order['get_cart_total'] += total

            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image_url': product.image_url,
                },
                'quantity' : cart[i]['quantity'],
                'get_total' : total
            }
            items.append(item)


    context = {'items': items, 'order':order , 'cartItems': cartItems}
    return render(request, 'cart/cart_details.html', context)

def cart_modal(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(   customer=customer, completed=False)
        items = order.cart_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}
    context = {'items': items, 'order':order }
    return render(request, 'cart/cart.html', context)