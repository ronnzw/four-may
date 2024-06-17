from django.db import models

from accounts.models import Customer
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
        Customer, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    order = models.ForeignKey(
        Order, 
        on_delete=models.SET_NULL,
        blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.customer.first_name} {self.customer.last_name}- {self.address}'