from . import views
from django.urls import path


app_name = 'products'
urlpatterns = [
    # getting products
    path('',views.product, name='product'),
    path('formal/', views.formal_product, name="formal"),
    path('casual/', views.casual_product, name="casual"),
    path('sports/', views.sports_product, name="sports"),
    path('shoes/', views.shoes_product, name="shoes"),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path("<int:pk>/", views.product_details, name="detail"),

    # wishlist
    path('wishlist/<int:product_id>/', views.wishlist, name='wishlist'),
    path('wishlist_products/', views.wishlist_products, name='wishlist-products'),
    path('wishlist/<int:product_id>/delete/', views.delete_wishlist_item, name='wishlist-delete')
]