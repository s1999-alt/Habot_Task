from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from .models import Employee
from .serializers import EmployeeSerializer



class EmployeeListCreateAPIView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    employees = Employee.objects.all()

    department = request.GET.get('department')
    role = request.GET.get('role')

    if department:
      employees = employees.filter(department=department)
    if role:
      employees = employees.filter(role=role)

    paginator = Paginator(employees, 10)
    page = request.GET.get('page', 1)
    employees = paginator.get_page(page)

    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class EmployeeDetailAPIView(APIView):

  def get_object(self, id):
    try:
      return Employee.objects.get(id=id)
    except Employee.DoesNotExist:
      return None
  
  def get(self, request, id):
    employee = self.get_object(id)
    if not employee:
      return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)
  
  def put(self, request, id):
    employee = self.get_object(id)
    if not employee:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id):
    employee = self.get_object(id)
    if not employee:
      return Response(status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return Response({"message": "Employee deleted"}, status=status.HTTP_204_NO_CONTENT)



