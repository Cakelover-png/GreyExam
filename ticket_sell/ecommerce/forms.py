from django.forms import ModelForm
from ecommerce.models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('ticket', 'price',)
