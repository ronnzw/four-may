from django.forms import ModelForm
from address.models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta:
        fields = ['mobile_number','alternative_mobile_number','address', 'city', 'province', 'zipcode']
        model = ShippingAddress


class DeliveryMethodForm(ModelForm):
    class Meta:
        fields = ['pickup_instore', 'store']
        model = ShippingAddress