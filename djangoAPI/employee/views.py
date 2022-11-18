from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
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

        return JsonResponse({'error': str(err), 'status': status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def createDepartment(request):
    serializer = DepartmentSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return JsonResponse({"data": serializer.data, 'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)

    return JsonResponse({'error': serializer.errors["DepartmentName"][0], 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updateDepartment(request, departmentId):
    try:
        departmentItem = Departments.objects.get(pk=departmentId)
        serializer = DepartmentSerializers(departmentItem, data=request.data)

    except Exception as err:
        return JsonResponse({'newData': str(err), 'status': status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()

        return JsonResponse({'update': serializer.data, 'status': status.HTTP_202_ACCEPTED}, status=status.HTTP_200_OK)

    return JsonResponse({'newData': serializer.errors["DepartmentName"][0], 'status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def departmentDelete(request, departmentId):
    try:
        departmentDetail = Departments.objects.get(pk=departmentId)
        serialized_detail = DepartmentSerializers(departmentDetail)
        departmentDetail.delete()

        return Response(serialized_detail.data, status=status.HTTP_202_ACCEPTED)

    except Exception as err:
        return JsonResponse({'error': str(err), 'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
