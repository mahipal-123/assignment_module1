from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.

from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    email= models.EmailField()
    firstname= models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    mobile= models.PositiveBigIntegerField()
    password= models.CharField(max_length=10)
    role=models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.firstname
    
class Product(models.Model):
    
    category=(
        ("Men","Men"),
        ("Women","Women"),
        ("Child","Child")
    )

    size=(
        ("S","S"),
        ("XS","XS"),
        ("M","M"),
        ("L","L"),
        ("XL","XL")
    )

    brand=(
        ("Levis","Levis"),
        ("Roadstar","Roadstar"),
        ("Nike","Nike"),
        ("Supreme","Supreme")
    )
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    pcategory=models.CharField(max_length=20,choices=category)
    psize=models.CharField(max_length=20,choices=size)
    pbrand=models.CharField(max_length=20,choices=brand)
    price=models.PositiveBigIntegerField()
    desc=models.TextField()
    picture=models.ImageField(default="",upload_to="P_Picture")
    pname=models.CharField(max_length=30)

    def __str__(self):
        return self.pname
    
class Wishlist(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.pname} || {self.user.firstname}"
    
class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty= models.IntegerField(default=1)
    product_price= models.FloatField()
    total_price= models.FloatField(default=0)
    payment_status= models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.firstname} || {self.product.pname}"
    
class Order(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()
    pincode=models.CharField(max_length=8)

    def __str__(self):
        return f"{self.user.firstname} {self.user.lastname}"
