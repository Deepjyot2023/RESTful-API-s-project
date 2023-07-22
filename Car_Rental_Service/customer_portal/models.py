

from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from cars_category_portal.models import *

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Booking_number = models.IntegerField()
    Customer_name  = models.CharField(max_length=20)
    Car_category   = models.CharField(max_length=20)
    Car_rental     = models.DateTimeField(auto_now_add=True)
    Car_mileage    = models.IntegerField()


    # def __str__(self):
    #     return self.Customer_name


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    Car_dealer    = models.ForeignKey(CarDealer, on_delete=models.PROTECT)
    Rent_return   = models.DateTimeField(auto_now_add=True)
    Cars_category = models.ForeignKey(CarCategories, on_delete=models.PROTECT)
    Days_return   = models.CharField(max_length = 3)
    customer      = models.ForeignKey(Customer, on_delete=models.PROTECT)
    is_complete   = models.BooleanField(default = False)


    # def __str__(self):
    #     return self.Cars_category





