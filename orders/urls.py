from . import views
from django.urls import path


app_name = 'orders'
urlpatterns = [
    path('',views.cart, name='cart'),
    path('update_item',views.update_item, name="update_item"),
    path('canvascontent', views.ajax_for_offcanvas, name='canvascontent'),
    path('checkout',views.checkout,name='checkout'),
    path('payment', views.payments, name='payment'),
    path('check-payment', views.check_payment, name='check-payment')
]