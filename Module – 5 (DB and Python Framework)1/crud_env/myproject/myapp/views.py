from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import random
import requests
from django.conf import settings
import razorpay
from django.views.decorators.cache import never_cache

# Create your views here.

# # seller viwes start 

@never_cache
def add_product(request):
    if request.POST:
        Product.objects.create(
            product_name = request.POST['product_name'],
            product_model = request.POST['model'],
            ram = request.POST['ram'],
            price = request.POST['price'],
            product_picture = request.FILES['product_picture'],
        )
        msg="Product Added Suceesfully"
        messages.success(request,msg)
        return render(request,"add_product.html")
    else:
        return render(request,"add_product.html")

@never_cache
def view_product(request):
    product = Product.objects.all()
    print("=============",product)
    return render(request,"view_product.html",{'product':product})

@never_cache
def product_details(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,"product_details.html",{'product':product})

@never_cache
def product_edit(request,pk):
    product=Product.objects.get(pk=pk)
    if request.POST:
        product.product_name = request.POST['product_name']
        product.product_model = request.POST['model']
        product.ram = request.POST['ram']
        product.price = request.POST['price']
       
        
        try:
                product.product_picture = request.FILES['product_picture']
        except:
            pass
        product.save()
        msg="Product Updated Suceesfully"
        messages.success(request,msg)
        return render(request,"product_edit.html",{'product':product})
    else:
        return render(request,"product_edit.html",{'product':product})

@never_cache
def product_delete(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    msg="Product Deleted Suceesfully"
    messages.success(request,msg)
    return redirect('view_product')

