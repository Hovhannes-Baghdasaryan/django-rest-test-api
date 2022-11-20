from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Departments, Employee
from .serializers import DepartmentSerializers, EmployeeSerializer, CreateEmployeeSerializer


@api_view(["GET"])
def getAllEmployees(_, departmentId):
    employees = Employee.objects.filter(DepartmentForeignId=departmentId)
    employees_serializer = EmployeeSerializer(employees, many=True)
    return Response(employees_serializer.data)


@api_view(["POST"])
def createEmployees(request, departmentId):
    try:
        final_request_data = {**request.data, "DepartmentForeignId": departmentId}

        employee_serializer = CreateEmployeeSerializer(data=final_request_data)

        if employee_serializer.is_valid():
            employee_serializer.save()

            final_show_data = {
                "EmployeeId": employee_serializer.data["EmployeeId"],
                "EmployeeName": employee_serializer.data["EmployeeName"],
            }

            return JsonResponse({'data': final_show_data, 'status': status.HTTP_201_CREATED},
                                status=status.HTTP_201_CREATED)

        return JsonResponse({'message': employee_serializer.errors, 'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

    except Exception as err:

        return JsonResponse({'mes': str(err), 'status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getDepartmentDetail(_, departmentId):
    try:
        departmentDetail = Departments.objects.get(pk=departmentId)
        department_serializer = DepartmentSerializers(instance=departmentDetail)

        return Response(department_serializer.data)

    except Exception as err:

        return JsonResponse({'error': str(err), 'status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def createDepartment(request):
    serializer = DepartmentSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return JsonResponse({"data": serializer.data, 'status': status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)

    return JsonResponse({'error': serializer.errors["DepartmentName"][0], 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updateDepartment(request, departmentId):
    try:
        departmentItem = Departments.objects.get(pk=departmentId)
        serializer = DepartmentSerializers(departmentItem, data=request.data)

    except Exception as err:
        return JsonResponse({'message': str(err), 'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()

        return JsonResponse({'data': serializer.data, 'status': status.HTTP_202_ACCEPTED}, status=status.HTTP_200_OK)

    return JsonResponse({'message': serializer.errors["DepartmentName"][0], 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)


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
