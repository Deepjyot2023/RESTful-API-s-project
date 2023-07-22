
from django.contrib import admin
from .models import CarDealer, CarCategories

# Register your models here.


class CarDealerAdmin(admin.ModelAdmin):
    list_display = ['car_dealer', 'phone_no', 'price']


class CarCategoriesAdmin(admin.ModelAdmin):
    list_display = ['Car_name', 'Compact_car', 'Premium_Car', 'Minivan_car', 'delear', 'capacity', 'is_available']


admin.site.register([CarDealer, CarCategories])



