

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from customer_portal.models import *
from cars_category_portal.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'customer/login.html')
    else:
        return render(request, 'customer/home_page.html')


# customer login
def login(request):
    return render(request, 'customer/login.html')



def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'customer/home_page.html')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

        try:
            customer = Customer.objects.get(user = user)
        except:
            customer = None
        if customer is not None:
            auth.login(request, user)
            return render(request, 'customer/home_page.html')
        else:
            return render(request, 'customer/login_failed.html')


# customer logout
def logout_view(request):
    auth.logout(request)
    return render(request, 'customer/login.html')


# customer registration
def register(request):
    return render(request, 'customer/register.html')



def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email    = request.POST['email']

    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'customer/registration_error.html')


    customer = Customer(user = user)   
    customer.save()
    return render(request, 'customer/registered.html')


@login_required
def search(request):
    return render(request, 'customer/search.html')



@login_required
def search_results(request):
    if request.method == 'POST':
        car_dealer = CarDealer.objects.filter(car = car)        
        car = request.POST['car']
        car = car.lower()
        cars_list = []    
    for car in car_dealer:
            cars = CarCategories.objects.filter(car = car)
            for car in cars:
                if car.is_available == True:
                    car_dictionary = {'Car_name':car.Car_name, 'Compact_car':car.Compact_car, 'Minivan_car': car.Minivan_car, 'id':car.id, 'capacity':car.capacity}
                    cars_list.append(car_dictionary)
            request.session['cars_list'] = cars_list
            return render(request, 'customer/search_results.html')



# Renting cars on per day basis calculation
@login_required
def rent_cars(request):
    if request.method == "POST":
        id = request.POST['id']
        car = CarCategories.objects.get(id = id)
        cost_per_day = int(car.capacity)*1.2
        return (request, 'customer/confirmation.html', {'car':car, 'cost_per_day':cost_per_day} )



# Confiramtion for rental basis cars per customer
@login_required
def confirm(request):
    if request.method == "POST":
        car_id = request.POST['id']
        username = request.user
        user = User.objects.get(username = username)
        Days_return = request.POST['Days_return']
        car = CarCategories.objects.get(id = car_id)
    if car.is_available:
        car_dealer = car.dealer
        Rent_return = (int(car.capacity))*1.7*(int(Days_return))
        car_dealer.price += Rent_return
        car_dealer.save()
        try:
            order = Orders(car = car, car_dealer = car_dealer, user = user, Rent_return=Rent_return, Days_return = Days_return)
            order.save()
        except:
            order = Orders.objects.get(car = car, car_dealer = car_dealer, user = user, Rent_return=Rent_return, Days_return=Days_return)
        car.is_available = False
        car.save()
        return render(request, 'customer/confirmed.html', {'order':order})
    else:
        return render(request, 'customer/order_failed.html')



@login_required
def manage_cars(request):
    order_list = []
    user = User.objects.get(username = request.user)
    try:
        orders = Orders.objects.filter(user = user)
    except:
        orders = None
    if orders is not None:
        for o in orders:
            if o.is_complete == False:
                order_dictionary = {'id':o.id,'days':o.Days_return, 'car':o.Cars_category, 'rent':o.Rent_return, 'car_dealer':o.Car_dealer}
                order_list.append(order_dictionary)
    return render(request, 'customer/manage.html', {'od':order_list})



@login_required
def update_order(request):
    if request.method == "POST":        
        order_id = request.POST['id']
        order = Orders.objects.get(id = order_id)
        car = order.car
        car.is_available = True
        car.save()

        Cardealer = order.Car_dealer
        Cardealer.price -= int(order.Rent_return)
        Cardealer.save()
        order.delete()
        cost_per_day = int(car.capacity)*1.7
        return render(request, 'customer/confirmation.html', {'car': car}, {'cost_per_day': cost_per_day})





































