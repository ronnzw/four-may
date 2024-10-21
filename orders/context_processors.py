from .utils import active_order
from products.models import WishList


def cart_and_wishlist_total(request):
    """Takes a request and returns the number of cart items
        and wishlist items
        
    Returns: 
        dict: cart_total and wishlist_total
    """
    cart_total = 0
    wishlist_total = 0

    if request.user.is_authenticated:
        context = active_order(request)
        order = context['order']
        cart_total = order.get_cart_items
        
        user = request.user
        wishlist_products = WishList.objects.filter(user=user)
        wishlist_total = wishlist_products.count()
    data = {'cart_total': cart_total, 'wishlist_total':wishlist_total}
    return data
