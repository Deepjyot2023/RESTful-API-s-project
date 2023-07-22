

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from cars_category_portal.models import *
from customer_portal.models import * 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'cars_category/login.html')
    else:
        return render(request, 'cars_category/home_page.html')


# login to car rental system
def login(request):
    return render(request, 'cars_category/login.html')


# checking users authentication
def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'cars_category/home_page.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            car_dealer = CarDealer.objects.get(car_dealer=user)
        except:
            car_dealer = None
        if car_dealer is not None:
            auth.login(request, user)
            return render(request, 'cars_category/home_page.html')
        else:
            return render(request, 'cars_category/login_failed.html')



# logout for user 
def logout_view(request):
    auth.logout(request)
    # print(auth)
    return render(request, 'cars_category/login.html')


# registering user
def register(request):
    return render(request, 'cars_category/register.html')


def registration(request):
    if request.method=='POST':
        username  = request.POST['username'] 
        password  = request.POST['password']
        firstname = request.POST['firstname']
        lastname  = request.POST['lastname']
        email     = request.POST['email']

    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = firstname
        user.last_name  = lastname
        user.save()
    except:
        return render(request, 'cars_category/registration_error.html')
    else:
        car_dealer = CarDealer(car_dealer = user)
    car_dealer.save()
    return render(request, 'cars_category/registered.html')



# adding car details
@login_required
def add_cars(request):
    if request.method=='POST':
        compct_car  = request.POST['compact_car']
        premium_car = request.POST['premium_car']
        minivan_car = request.POST['minivan_car']
        car_dealer  = CarDealer.objects.get(car_dealer=request.user)
        phone_no    = phone_no
        capacity    = request.POST['capacity']

        try:
            price = CarDealer.objects.get(phone_no=phone_no)
        except:
            price = None
        if price is not None:
            cars = CarCategories(compct_car=compct_car, premium_car=premium_car, minivan_car=minivan_car, car_dealer=car_dealer, capacity=capacity)
        else:
            price = CarDealer(phone_no=phone_no)
            price.save()
            cars = CarDealer(compct_car=compct_car, premium_car=premium_car, minivan_car=minivan_car, car_dealer=car_dealer, capacity=capacity)

        cars.save()
        return render(request, 'cars_category/cars_added.html')



# managing car orders
@login_required
def manage_cars(request):
    username = request.user
    user = User.objects.get(username=username)
    car_dealer = CarDealer.objects.get(car_dealer = user)
    
    cars_list = []
    cars = CarCategories.objects.filter(dealer = car_dealer)
    for c in cars:
        cars_list.append(c)
    return render(request, 'cars_category/manage.html', {'cars_list': cars_list} )



@login_required
def order_list(request):
    username = request.user
    user = User.objects.get(username = username)
    car_dealer = CarDealer.objects.get(car_dealer = user)
    orders = Orders.objects.filter(car_dealer = car_dealer)

    order_list = []
    for o in orders:
        if o.is_complete == False:
            order_list.append(o)
    return render(request, 'cars_category/order_list.html')

    

@login_required
def complete(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    cars  = order.cars
    order.is_complete = True
    order.save()
    cars.is_available = True
    cars.save()
    return HttpResponseRedirect('cars_category/order_list/')



@login_required
def delete(request):
    car_id = request.POST['id']
    car = CarCategories.objects.get(id = car_id)
    car.delete()
    return HttpResponseRedirect(request, 'cars_category/manage_cars/')






























