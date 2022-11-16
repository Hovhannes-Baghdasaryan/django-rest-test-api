from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Departments
from .serializers import EmployeeSerializer, DepartmentSerializers


@api_view(["GET"])
def getAllDepartments(request):
    departments = Departments.objects.all()
    department_serializer = DepartmentSerializers(departments, many=True)
    return Response(department_serializer.data)


@api_view(["POST"])
def createDepartment(request):
    serializer = DepartmentSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, template_name="Hovo")
