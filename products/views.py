from django.shortcuts import get_object_or_404, render
from .models import Product, ProductVariant
from orders.models import Order

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'products/product_list.html', context)

def formal_product(request):
    products = Product.objects.filter(category="F")
    context = {'products': products}
    return render(request,'products/formal.html', context)

def casual_product(request):
    products = Product.objects.filter(category="C")
    context = {'products': products}
    return render(request,'products/casual.html', context)

def sports_product(request):
    products = Product.objects.filter(category="S")
    context = {'products': products}
    return render(request,'products/sports.html', context)

def shoes_product(request):
    products = Product.objects.filter(category="SH")
    context = {'products': products}
    return render(request,'products/shoes.html', context)

def product_details(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}
  

    product = get_object_or_404(Product, pk=pk)
    context = {'product': product, 'items': items, 'order':order}

    if product.variant != 'None':
        if request.method == 'POST': #if we select color
            variant_id = request.POST.get('variantid')
            variant = ProductVariant.objects.get(id=variant_id)
            colors = ProductVariant.objects.filter(product_id=pk,size_id=variant.size_id )
            size = ProductVariant.objects.raw('SELECT * FROM  products_productvariant  WHERE product_id=%s GROUP BY size_id',[pk])

        else:
            variants = ProductVariant.objects.filter(product_id=pk)
            colors = ProductVariant.objects.filter(
                product_id=product.id, 
                size_id=variants[0].size_id
                )

            size = ProductVariant.objects.raw(
                'SELECT * FROM products_productvariant WHERE product_id=%s GROUP BY size_id',[pk]
                )
            variant =ProductVariant.objects.get(id=variants[0].id)
        context.update({'colors': colors, 'variant': variant, 'sizes': size})

    return render(request, 'products/details.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = ProductVariant.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('products/color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)