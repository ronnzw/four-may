from django.contrib import admin

from .models import Order, OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','product_variant_size','product_variant_size','quantity','date_added']

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'customer', 'completed','date_ordered']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
