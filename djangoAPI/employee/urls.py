from django.urls import path

from . import views

urlpatterns = [
    path('department/', views.getAllDepartments),
    path('department/create', views.createDepartment)
]