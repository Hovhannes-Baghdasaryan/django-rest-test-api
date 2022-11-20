from django.http import JsonResponse
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Departments, Employee
from .serializers import DepartmentSerializers, EmployeeSerializer, CreateEmployeeSerializer, \
    IncrementCountDepartmentSerializers, DeleteDepartmentSerializers, CreateDepartmentSerializers

from drf_yasg import openapi


@method_decorator(name="get", decorator=swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            'post_slug', openapi.IN_QUERY,
            description=("Employee of a single department"),
            type=openapi.TYPE_STRING
        )
    ]
))
class PingView(APIView):
    def get(self, *args, **kwargs):
        return Response([{'ping': 'pong'}], status=status.HTTP_200_OK)


@api_view(["GET"])
def getAllEmployees(_, departmentId):
    employees = Employee.objects.filter(DepartmentForeignId=departmentId)
    employees_serializer = EmployeeSerializer(employees, many=True)
    return Response(employees_serializer.data)


@api_view(["POST"])
def createEmployees(request, departmentId):
    try:
        final_request_data = {**request.data, "DepartmentForeignId": departmentId}

        departmentItem = Departments.objects.get(pk=departmentId)

        edit_department_employee_count_data = {
            "EmployeeCount": departmentItem.EmployeeCount + 1
        }

        department_serializer = IncrementCountDepartmentSerializers(departmentItem,
                                                                    data=edit_department_employee_count_data)
        employee_serializer = CreateEmployeeSerializer(data=final_request_data)

    except Exception as err:

        return JsonResponse({'mes': str(err), 'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

    if employee_serializer.is_valid() and department_serializer.is_valid():
        employee_serializer.save()
        department_serializer.save()

        final_show_data = {
            "EmployeeName": employee_serializer.data["EmployeeName"],
        }

        return JsonResponse({'data': final_show_data, 'status': status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)

    return JsonResponse(
        {'message': employee_serializer.errors or department_serializer.errors, 'status': status.HTTP_400_BAD_REQUEST},
        status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getDepartmentDetail(_, departmentId):
    try:
        departmentDetail = Departments.objects.get(pk=departmentId)
        department_serializer = DepartmentSerializers(instance=departmentDetail)

        return Response(department_serializer.data)

    except Exception as err:

        return JsonResponse({'error': str(err), 'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def createDepartment(request):
    serializer = CreateDepartmentSerializers(data=request.data)

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
def departmentDelete(_, departmentId):
    try:
        departmentDetail = Departments.objects.get(pk=departmentId)
        serialized_detail = DeleteDepartmentSerializers(departmentDetail)
        departmentDetail.delete()

        return Response(serialized_detail.data, status=status.HTTP_202_ACCEPTED)

    except Exception as err:
        return JsonResponse({'error': str(err), 'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
