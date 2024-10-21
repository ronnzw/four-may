from django.db import models
from django.contrib.auth.models import User

from orders.models import Order


class InstorePickUpPoint(models.Model):
    COUNTRY_CHOICES = [
        ('Nam', 'Namibia'),
        ('SA', 'South Africa'),
        ('Zim', 'Zimbabwe')
    ]
    shop_name = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.shop_name


class ShippingAddress(models.Model):
    pickup_instore = models.BooleanField(default=False)
    store = models.ForeignKey(InstorePickUpPoint, 
                              on_delete=models.CASCADE, 
                              blank=True, null=True)
    customer = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    order = models.ForeignKey(
        Order, 
        on_delete=models.SET_NULL,
        blank=True, null=True)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)
    alternative_mobile_number = models.CharField(max_length=10, null=True,blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Delivery address for: {self.customer}'