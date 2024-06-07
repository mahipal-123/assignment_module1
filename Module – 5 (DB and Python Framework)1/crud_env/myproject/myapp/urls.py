"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('', views.view_product, name='view_product'),
    path('product_details/ <int:pk>/', views.product_details, name='product_details'),
    path('product_edit/ <int:pk>/', views.product_edit, name='product_edit'),
    path('product_delete/ <int:pk>/', views.product_delete, name='product_delete'),
    
]
