from django.urls import path

from . import views

urlpatterns = [
    path('department/create', views.createDepartment),
    path('department/<departmentId>', views.getDepartmentDetail),
    path('department/<departmentId>/delete', views.departmentDelete),
    path('department/<departmentId>/update', views.updateDepartment),
    path('department/<departmentId>/employee', views.getAllEmployees),
    path('department/<departmentId>/employee/create', views.createEmployees)
]
