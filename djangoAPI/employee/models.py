from django.db import models


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=40)
    EmployeeCount = models.IntegerField(auto_created=True, default=0)

    def __str__(self):
        return f"{self.EmployeeCount}"


class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=40)
    DepartmentForeignId = models.ForeignKey(Departments, on_delete=models.CASCADE)
