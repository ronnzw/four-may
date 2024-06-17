from django.db import models

from orders.models import Order
from products.models import Product, Size, Color


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default='', null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default='', null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.product.name
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total