from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from orders.models import Order


# Create your views here.
@login_required
def profiles(request):
    context = {}
    return render(request,'profile.html', context)

@login_required
def profile_dashboard(request):
    user = request.user
    orders = Order.objects.filter(customer=user,completed=True).order_by('-completed_date')
    orders_total = orders.count()
    if orders:
        most_recent_order = orders.first()
        items = (most_recent_order.orderitem_set.all()).order_by('-date_added')
    else:
        items = None
    context = {'orders': orders_total, 'items': items, 'sys_orders': orders}
    return render(request,'accounts/dashboard.html', context )
