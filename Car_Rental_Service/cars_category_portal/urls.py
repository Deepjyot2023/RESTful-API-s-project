

from django.urls import path, include
from cars_category_portal.views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^index/$', index),
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout_view),
    url(r'^register/$', register),
    url(r'^registration/$', registration),
    url(r'^add_cars/$', add_cars),
    url(r'^manage_cars/$', manage_cars),
    url(r'^order_list/$', order_list),
    url(r'^complete/$', complete),  
    url(r'^delete/$', delete),  


]



























