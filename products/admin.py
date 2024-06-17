from django.contrib import admin

# Register your models here.
from .models import Product, Category, Size, Color, ProductVariant


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['pk','product', 'size', 'color']


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant



class ColorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'code', 'color_tag']


class SizeAdmin(admin.ModelAdmin):
    list_display = ['pk','name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'variant','image_tag']
    inlines = [ProductVariantInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)