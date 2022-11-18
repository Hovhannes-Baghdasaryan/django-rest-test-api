from django.urls import path

from . import views

urlpatterns = [
    path('department/', views.getAllDepartments),
    path('department/create', views.createDepartment),
    path('department/<departmentId>', views.getDepartmentDetail),
    path('department/<departmentId>/delete', views.departmentDelete),
    path('department/<departmentId>/update', views.updateDepartment)
]
