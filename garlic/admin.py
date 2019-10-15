from django.contrib import admin
from garlic.models import Item
from garlic.models import Order
from garlic.models import PickupLocations


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','description','price')
    
    #Rearrange the fields inside the admin record for easier viewing
    fieldsets = (
        ('Bundle Details', {
            'fields': ['name',('description','total')]
        }),
    )

admin.site.register(Item, ItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('supporter','purchase','total','price','count','pickupLocation','email','order_date')
    
    #Rearrange the fields inside the admin record for easier viewing
    fieldsets = (
        ('Personal Info', {
            'fields': ['supporter','email', 'pickupLocation']
        }),
        ('Order Details', {
            'fields': ['purchase',('count','price','total')]
        }),        
    )
admin.site.register(Order, OrderAdmin)



admin.site.register(PickupLocations)

