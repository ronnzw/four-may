import json
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from cart.models import Cart
from products.models import Product, ProductVariant
from .models import Order, OrderItem
from .forms import ShippingAddressForm, DeliveryMethodForm


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}
    context = {'items': items, 'order':order}
    return render(request, 'orders/cart_details.html', context)


def checkout(request):
    pickup_form = DeliveryMethodForm()
    form = ShippingAddressForm()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}
    context = {'items': items, 'order':order,'form': form, 'pickup_form': pickup_form}
    return render(request, 'orders/checkout.html', context)   

def carted(request):
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


def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    variant_id = data['variantId']
    size_id = data['sizeId']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    if product.variant == "Size":
        product_variant = ProductVariant.objects.filter(product_id=product_id ,size_id=size_id)[0]

    else:
        product_variant = ProductVariant.objects.get(id=variant_id)

    order, created = Order.objects.get_or_create(
        customer=customer, completed=False)
       
    
    cartItem, created = OrderItem.objects.get_or_create(
        order=order, product=product, product_variant=product_variant)
    

    if action == 'add':
        cartItem.quantity = (cartItem.quantity + 1 )

    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1 )

    cartItem.save() 
    un_serialised_data = {
        'quantity': cartItem.quantity, 
        'itemTotal': str(cartItem.get_total), 
        'grandTotal': str(cartItem.order.get_cart_total), 'cartTotal': cartItem.order.get_cart_items
        }

    if cartItem.quantity <= 0:
        cartItem.delete()
        un_serialised_data = {
            'quantity': 0, 
            'itemTotal': 0, 
            'grandTotal': 0, 
            'cartTotal': 0
            }

    context = json.dumps(un_serialised_data)
    return JsonResponse(context, safe=False)


def ajax_for_offcanvas(request):
    data = {}
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()

        context = {'items': items, 'order': order}
        data = {'render_ajax': render_to_string('products/offcanvas.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)