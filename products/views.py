from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy

from .models import Product, ProductVariant, WishList
from orders.utils import active_order


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
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY

    context = active_order(request)
    product = get_object_or_404(Product, pk=pk)
    context.update({'product': product})

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
            variant = ProductVariant.objects.get(id=variants[0].id)
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

@login_required
def wishlist_products(request):
    user = request.user
    wishlist_products = WishList.objects.filter(user=user)
    context = {'wishlist_products': wishlist_products }
    return render(request, 'products/wishlist.html',context)

@login_required
def wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = WishList.objects.get_or_create(user=request.user, product=product)

    if not created:
        wishlist_item.delete()
        added_to_wishlist = False
    else:
        added_to_wishlist = True

    return JsonResponse({'added_to_wishlist': added_to_wishlist})

@login_required
def delete_wishlist_item(request, product_id):
    wishlist_item = get_object_or_404(WishList,product_id=product_id)

    try:
        if wishlist_item.user != request.user:
            return HttpResponseForbidden()
        else:
            wishlist_item.delete()
            return redirect('products:wishlist-products')

    except Exception as e:
        return HttpResponseServerError( f'{e} An error occurred while trying to delete the item.')


