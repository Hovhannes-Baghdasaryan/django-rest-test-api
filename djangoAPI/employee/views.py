from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Departments
from .serializers import DepartmentSerializers


@api_view(["GET"])
def getAllDepartments(request):
    departments = Departments.objects.all()
    department_serializer = DepartmentSerializers(departments, many=True)
    return Response(department_serializer.data)


@api_view(["GET"])
def getDepartmentDetail(request, departmentId):
    try:
        departmentDetail = Departments.objects.get(pk=departmentId)
        department_serializer = DepartmentSerializers(instance=departmentDetail)

        return Response(department_serializer.data)
    except Exception as err:

        raise ValidationError(detail=err)


@api_view(["POST"])
def createDepartment(request):
    serializer = DepartmentSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def departmentDelete(request, departmentId):
    try:
        departmentDetail = Departments.objects.get(pk=departmentId)
        serialized_detail = DepartmentSerializers(departmentDetail)
        departmentDetail.delete()

        return Response(serialized_detail.data, status=status.HTTP_202_ACCEPTED)

    except Exception as err:
       raise ValidationError(detail=err)