from . import views
from django.urls import path


app_name = 'products'
urlpatterns = [
    path('',views.product, name='product'),
    path('formal/', views.formal_product, name="formal"),
    path('casual/', views.casual_product, name="casual"),
    path('sports/', views.sports_product, name="sports"),
    path('shoes/', views.shoes_product, name="shoes"),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path("<int:pk>/", views.product_details, name="detail"),
]