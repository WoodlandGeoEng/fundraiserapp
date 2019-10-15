from django.db import models
from django.urls import reverse
import datetime
   
# Model representing items available in the fundraiser.
class Item(models.Model):
    
    """Columns in the Available Items Database"""
    name = models.CharField(max_length = 20, help_text = 'Item name.')
    description = models.CharField(max_length = 100, help_text = 'Brief description of item.')
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text='Unit price of item')

    def __str__(self):
        #String for representing the Model object.
        return self.name


      
# Create default items for the fundraiser if the item does not exist yet.
# Removing the defalut would make it versatile for any fundraiser.
check = Item.objects.filter(name="Bundle 1").first()
if check == None:
	record = Item(name="Bundle 1", description = '1 lbs Gourmet Garlic', price = 20.00)
	record.save()
else:
	pass

check = Item.objects.filter(name="Bundle 2").first()
if check == None:
	record = Item(name="Bundle 2", description = '2 lbs Gourmet Garlic', price = 30.00)
	record.save()
else:
	pass	

check = Item.objects.filter(name="Bundle 3").first()
if check == None:
	record = Item(name="Bundle 3", description = '3 lbs Gourmet Garlic', price = 40.00)
	record.save()
else:
	pass

class PickupLocations(models.Model):
    """Model representing pickup locations."""
    location = models.CharField(max_length = 50, help_text = 'Location description')
    
    def __str__(self):
        #String for representing the Model object.
        return self.location

class Order(models.Model):
    """Model base for order instances via forms."""
    
    """Columns in the Available Items Database"""
    supporter = models.CharField(max_length = 40, help_text = 'Supporter name')
    order_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, unique=True)
    purchase = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(default = 1)
    pickupLocation = models.ForeignKey('PickupLocations',on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places = 2, max_digits = 4, default=30.00)
    
    def total_amount(self):
       return self.count * self.price
    total = property(total_amount)


    def __str__(self):
        #String for representing the Model object.
        return self.supporter	

  