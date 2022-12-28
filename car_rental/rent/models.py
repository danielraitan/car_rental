from django.db import models
from datetime import datetime    

    
class CarInfo(models.Model):
    car_image = models.URLField()
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)    
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.car_brand}, {self.car_model}'
    
class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
    