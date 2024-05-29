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
from.import views

urlpatterns = [
    
    path("",views.index, name="index"),
    path("sindex",views.sindex, name="sindex"),
    path("about",views.about, name="about"),
    path("blog",views.blog, name="blog"),
    path("contact",views.contact, name="contact"),
    path("shop/<str:cat>",views.shop, name="shop"),
    path("signup",views.signup, name="signup"),
    path("login",views.login, name="login"),
    path("logout",views.logout, name="logout"),
    path("fpassword",views.fpassword, name="fpassword"),
    path("fpassword_email",views.fpassword_email, name="fpassword_email"),
    path('password', views.password, name='password'),
    path('email_newpassword', views.email_newpassword, name='email_newpassword'),
    path("newpassword",views.newpassword, name="newpassword"),
    path("otp",views.otp, name="otp"),
    path("changepassw",views.changepassword, name="changepass"),
    path("profile_edit",views.profile, name="profile_edit"),
    path("addproduct",views.addproduct, name="addproduct"),
    path("viewproduct/<str:cat>",views.viewproduct, name="viewproduct"),
    path("pdetail/ <int:pk>",views.pdetail, name="pdetail"),
    path("edit/ <int:pk>",views.edit, name="edit"),
    path("delete/ <int:pk>",views.delete, name="delete"),
    path("bpdetail/ <int:pk>",views.bpdetail, name="bpdetail"),
    path("wishlist",views.wishlist, name="wishlist"),
    path("addwish/ <int:pk>",views.addwish, name="addwish"),
    path("removewish/ <int:pk>",views.removewish, name="removewish"),
    path("scart",views.scart, name="scart"),
    path("addcart/ <int:pk>",views.addcart, name="addcart"),
    path("removecart/ <int:pk>",views.removecart, name="removecart"),
    path("change_qty",views.change_qty, name="change_qty"),
    path("checkout",views.checkout_detail,name="checkout"), 
    path("success",views.success,name="success"),
    path("myorder",views.myorder,name="myorder")
]
