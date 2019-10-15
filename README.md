# fundraiserapp
by woodlangGeoEng

## This is a simple app with 3 Django models that allows a user to input an order in a fundraising event for a non-profit organization.
You may use this code, but the creater bears no responsability for outcomes as a result of its use. The app is currently preloaded for a garlic fundraiser, but that can be changed in the model.py file.

The admin tool is the primary means to track and view available items and orders. 
A view form is available for users to enter their contact information and order choice.
***

Dependencies:
<br>Python 3.6
<br> Django 2.2.6
<br> For windows, use pip to install the latest version of Django:
<br> pip install Django==2.2.6
<br> Link can also be found here: https://www.djangoproject.com/download/

## Getting Started:

1. Copy the entire fundraiserapp directory to your working directory.

2. In Command Prompt, navigate to the root folder (the folder containing manage.py) and run `python manage.py migrate` to create the database models.

3. Create a superuser with 'python manage.py createsuperuser' and follow the prompts to enter a username and password.

4. Start the development server with 'python manage.py runserver' and visit http://127.0.0.1:8000/admin/
   to create more users, items, pickup locations and orders.

5. Visit http://127.0.0.1:8000/garlic/ to see the welcome (index) page (Link to order form coming next!).

6. Visit http://127.0.0.1:8000/garlic/order/ to enter an order as a user. (Purchase confirmation and summary coming next!)

7. Tests can be found in mysite/garlic/tests.py 
    Some are functional, some arn't quite there yet. More work coming here too!
