from django.db import models
from django.utils import timezone

# Create your models here.
    
class Product(models.Model):
    product_model = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    ram = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    description = models.TextField()
    product_picture = models.ImageField(default="IMAGE NOT FOUND",upload_to="product/")

    def __str__(self):
        return self.product_name 
