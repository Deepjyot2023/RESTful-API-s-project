

from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

# Create your models here.

class CarDealer(models.Model):
    car_dealer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no   = models.CharField(validators= [MinLengthValidator(10), MaxLengthValidator(13)], max_length=20)
    price      = models.IntegerField(default = 0)



class CarCategories(models.Model):
    Car_name     = models.CharField(max_length=20, default=True)
    Compact_car  = models.CharField(max_length = 20)
    Premium_car  = models.CharField(max_length = 20)
    Minivan_car  = models.CharField(max_length = 20)
    dealer       = models.ForeignKey(CarDealer, on_delete=models.PROTECT)   # one-to-many relation with dealer
    capacity     = models.CharField(max_length = 2)
    is_available = models.BooleanField(default = True)







