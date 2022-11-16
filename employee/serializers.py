from .models import Employee, Departments
from rest_framework import serializers


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        field = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')
