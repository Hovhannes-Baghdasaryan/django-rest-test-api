from .models import Employee, Departments
from rest_framework import serializers


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"


class CreateDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ("DepartmentName", )


class DeleteDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentName', "EmployeeCount")


class IncrementCountDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ("EmployeeCount",)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("EmployeeId", "EmployeeName")


class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("EmployeeName", "DepartmentForeignId")
