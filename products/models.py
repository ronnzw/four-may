from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe


class Category(models.Model):
    CATEGORY_CLASSES = [
        ('F', 'Formal'),
        ('C', 'Casual'),
        ('S', 'Sports'),
        ('SH', 'Shoes'),
    ]
    name = models.CharField(max_length=2,choices=CATEGORY_CLASSES,default="F")

    class Meta:
        verbose_name = "Categorie"

    def __str__(self):
        return self.name


class Size(models.Model):
    ''' Size model to allow addition of new sizes '''
    name = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    """All available colors in the system"""
    name = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=7, blank=True, null=True)

    def color_tag(self):
        if self.code is not None:
            return mark_safe(f'<p style="background-color:{self.code}">color</p>')
        else:
            return ""

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product has a list of products in our inventory"""
    CATEGORY_CLASSES = [
        ('F', 'Formal'),
        ('C', 'Casual'),
        ('S', 'Sports'),
        ('SH', 'Shoes'),
    ]

    VARIANTS = [
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),
    ]
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.CharField(
        max_length=2, choices=CATEGORY_CLASSES, default="F"
        )
    variant = models.CharField(
    max_length=10, choices=VARIANTS, default="None"
    )
    image = models.ImageField(upload_to='uploads/product/',null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})
    
    
    @property
    def image_url(self):
        try:
            url = self.image.url
        except ValueError:
            url = ''
        return url
    
    def image_tag(self):
        if self.image_url != '':
            return mark_safe(f'<img src="{self.image_url}" height="50" />')
        else:
            return ''


class ProductVariant(models.Model):
    """Variant of the product. i.e. Size, Color or both"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)          

    def __str__(self):
        return f"{self.product.name}"
    

class WishList(models.Model):
    """Items that the users was to buy later"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}" 