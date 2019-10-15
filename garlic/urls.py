from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


# Order form view:
urlpatterns += [   
    path('order/', views.OrderCreate, name='OrderCreate'),    
]
