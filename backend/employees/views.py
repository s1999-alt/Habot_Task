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
  




