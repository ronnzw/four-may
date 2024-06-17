from django.contrib import admin

from .models import ShippingAddress, InstorePickUpPoint


admin.site.register(ShippingAddress)
admin.site.register(InstorePickUpPoint)