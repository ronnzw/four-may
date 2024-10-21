import json

from decouple import config
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from paynow import Paynow

from address.models import ShippingAddress
from products.models import Product, ProductVariant
from .forms import ShippingAddressForm, DeliveryMethodForm
from .models import Order, OrderItem
from .utils import active_order, currency_session_value, process_payment


paynow = Paynow(
    config('INTEGRATION_ID', default=''), 
    config('INTEGRATION_KEY', default=''),
    config('PAYNOW_REQUEST_URL', default=''),
    config('PAYNOW_RESPONSE_URL', default='')
    )


@login_required
def cart(request):
    context = active_order(request)
    return render(request, 'orders/cart_details.html', context)

@login_required
def checkout(request):
    order_details = active_order(request)
    order = order_details['order']
    context = order_details
    user = request.user
    shipping_address = ShippingAddress(customer=user,order=order)
    form = ShippingAddressForm(request.POST or None, instance=shipping_address)
    pickup_form = DeliveryMethodForm(request.POST or None, instance=shipping_address)
    if pickup_form.is_valid():
        form_data = pickup_form.save(commit=False)
        if form_data.pickup_instore != False:
            form_data.save()
            pickup_form = DeliveryMethodForm()
            messages.success(request,'Thank you, we got your pickup point, proceed to order')
        elif form.is_valid():
            form.save()
            messages.success(request,'Thank you, we got your address, proceed to order')
            form = ShippingAddressForm()

    context.update({'form': form, 'pickup_form': pickup_form})
    return render(request, 'orders/checkout.html', context)   

@login_required
def update_item(request):
    '''Add or Removes items from the cart'''
    data = json.loads(request.body)
    product_id, action, variant_id  = data['productId'], data['action'], data['variantId']

    currency_session_value(request)

    product = get_object_or_404(Product,id=product_id)
    product_variant = get_object_or_404(ProductVariant, id=variant_id)
    order_details = active_order(request)
    order = order_details['order']
    # Creating cart item
    cartItem, created = OrderItem.objects.get_or_create(
        order=order, product=product, product_variant=product_variant
        )

    if action == 'add':
        cartItem.quantity = (cartItem.quantity + 1 )
    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1 )

    cartItem.save()
    # Pass filter in html
    price_with_currency = render_to_string(
        'orders/itemtotal.html', {'price': cartItem.get_total, 'curr': currency_session_value(request) }
        )
    grand_total_with_currency = render_to_string(
        'orders/itemtotal.html', {'price': cartItem.order.get_cart_total, 'curr': currency_session_value(request) }
        )
    un_serialised_data = {
        'price_with_currency': price_with_currency,
        'grand_total_with_currency': grand_total_with_currency,
        'quantity': cartItem.quantity, 
        'itemTotal': str(cartItem.get_total), 
        'grandTotal': str(cartItem.order.get_cart_total), 'cartTotal': cartItem.order.get_cart_items
        }
    # Delete item from cart is quantity is less than zero
    if cartItem.quantity <= 0:
        cartItem.delete()
        un_serialised_data = {
            'price_with_currency': price_with_currency,
            'grand_total_with_currency': grand_total_with_currency,
            'quantity': 0, 
            'itemTotal': 0, 
            'grandTotal': 0, 
            'cartTotal': 0
            }

    context = json.dumps(un_serialised_data)
    return JsonResponse(context, safe=False)

@login_required
def ajax_for_offcanvas(request):
    try:
        context = active_order(request)
        ajax_render = render_to_string('orders/offcanvas.html',{'items': context['items']})
        raw_data = {'ajax_render': ajax_render}
        data = json.dumps(raw_data)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return e
    

@login_required
def payments(request):
    customer_order = active_order(request)
    items, order = customer_order.values()
    response = process_payment(paynow,items,order,request.user.email)

    if response.success:
        order.payment_status = response.poll_url
        order.save()
        return redirect(response.redirect_url)
    else:
        error_message = response.error
        messages.warning(request,f'Sorry, something went wrong with our payment partner, refresh & try again but you do not need to capture your address again. {error_message}')
        return redirect('orders:checkout')
        
@login_required
def check_payment(request):
    paynow_status = ("paid", "awaiting delivery", "delivered")
    order_details = active_order(request)
    order = order_details['order']
    current_order = Order.objects.get(id=order.id)
    status = paynow.check_transaction_status(order.payment_status)
    clean_status = (status.status).lower()

    if clean_status in paynow_status:
        try:
            current_order.complete_order(clean_status)
            messages.info(request, f'Transaction completed successfully, you paid {status.amount}')
            # Sending email to the user
            current_order.send_order_completion_email()
            return redirect('accounts:dashboard')
                    
        except Exception as e:
            messages.warning(request, f'Sorry we failed to update your order. Contact us please for a refund or order rectification.Error: {e}')
            return redirect('accounts:dashboard')            
                   
    else:
        error_message = status.status
        messages.warning(request, f'Transaction failed:  {error_message}. You may try again')
        return redirect('orders:checkout')