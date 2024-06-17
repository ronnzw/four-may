from django.forms import ModelForm
from address.models import ShippingAddress, InstorePickUpPoint

class ShippingAddressForm(ModelForm):
    class Meta:
        fields = ['address', 'city', 'province', 'zipcode']
        model = ShippingAddress


class DeliveryMethodForm(ModelForm):
    class Meta:
        fields = ['pickup_instore', 'store']
        model = ShippingAddress