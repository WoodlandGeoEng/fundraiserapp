from django.forms import ModelForm

from .models import Order


class NewOrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
        