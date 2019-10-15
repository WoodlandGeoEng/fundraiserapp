

from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcome to our Garlic Fundraiser!")




from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.urls import reverse_lazy
import datetime
from garlic.forms import NewOrderForm

def OrderCreate(request):
 
    if request.method == "POST":
        form = NewOrderForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
            #return redirect('/thanks') - not fully implemented
 
    else:
 
        form = NewOrderForm()
 
        return render(request, "OrderCreate.html", {'form': form})

'''
# Call the thank you and payment summary page. Not quite implemented.
def thanks(request):
    return render(request, "thank_you.html", model_instance)        

'''