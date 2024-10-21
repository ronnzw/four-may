import uuid

from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

from products.models import Product, ProductVariant


class Order(models.Model):
    """Order of the customer. Only one active at a time"""
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, editable=False, unique=True)
    payment_status = models.CharField(max_length=200, blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    paynow_status = models.CharField(max_length=50, blank=True, null=True) 

    def __str__(self):
        return str(self.id)
    
    def complete_order(self, paynow_status):
        """Mark the order as completed and update necessary fields."""
        self.completed = True
        self.completed_date = datetime.now()
        self.paynow_status = paynow_status
        self.save()
    
    def save(self, *args, **kwargs):
        """Generate a transaction id for items without an id"""
        if not self.transaction_id:
            self.transaction_id = self.generate_transaction_id()
        super().save(*args, **kwargs)
    
    def send_order_completion_email(self):
        """Send an email notification to the user when the order is completed."""
        if self.customer and self.customer.email:
            subject = 'Order Completed Successfully'
            message = f'Hi {self.customer.first_name},\n\nYour order with transaction ID: {self.transaction_id} has been completed successfully.\n\n Thank you for shopping with 4May International!\n\n Yours faithful,\n\n 4May International sales team'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [self.customer.email]

            # Send the email
            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                return e

    def generate_transaction_id(self):
        return str(uuid.uuid4())
    
    @property
    def get_cart_total(self):
        """Takes no args and returns the total amount in cart
        
        Returns:
            int: Total amount of items in the cart
        """
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        """Takes no args and returns the number of items in cart
        
        Returns:
            int: Total number of items in the cart 
        """
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    

class OrderItem(models.Model):
    """Represent items of an order i.e. items in a cart"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.product.name
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    @property
    def product_variant_size(self):
        return f'{self.product_variant.size.name}'
    
    @property
    def product_variant_color(self):
        return f'{self.product_variant.color.name}'