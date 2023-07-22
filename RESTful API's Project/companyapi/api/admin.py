
from django.contrib import admin
from api.models import Company, Employee

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')



admin.site.register([Company, Employee])















