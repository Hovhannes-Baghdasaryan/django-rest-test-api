from django.db import models


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=40)


class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=20)

