
from rest_framework import serializers
from api.models import Company
from api.models import Employee

# Create serializers here;


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = "__all__" 



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"












