from django.test import TestCase
import datetime
from django.utils import timezone


from .models import Order
class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Order.objects.create(supporter='Sue Jones')

    def test_supporter_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('supporter').max_length
        self.assertEquals(max_length, 40)    

    def test_supporter_label(self):
        order = Order.objects.get(id=1)
        test_label = order._meta.get_field('supporter').verbose_name
        self.assertEquals(test_label, 'supporter')  

    def test_total_is_correct(self):
        cost = 20
        count = 3
        
        total = order._meta.get_field('supporter').verbose_name
        self.assertEquals(test_label, 'supporter')       
 
   

from garlic.forms import NewOrderForm
class OrderFormTest(TestCase):

    def test_order_form_order_date_is_valid(self):
        date = datetime.date.today()
        form = NewOrderForm(data={'order_date': date})
        self.assertTrue(form.is_valid())


""" Test page view urls"""

class pageViewTest(TestCase):

    def test_order_url_exists_at_desired_location(self):
        response = self.client.get('/garlic/order/')
        self.assertEqual(response.status_code, 200)

    def test_thanks_url_exists_at_desired_location(self):
        response = self.client.get('/garlic/thanks/')
        self.assertEqual(response.status_code, 200)    