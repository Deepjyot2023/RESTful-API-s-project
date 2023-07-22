
from django.contrib import admin
from .models import Customer, Orders

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'Booking_number', 'Customer_name', 'Car_category', 'Car_rental', 'Car_mileage']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user', 'Car_dealer', 'Rent_return', 'Cars_category', 'Days_return']


admin.site.register([Customer, Orders])

