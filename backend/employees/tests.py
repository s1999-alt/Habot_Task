from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()


class EmployeeTests(APITestCase):

  def setUp(self):
    self.user = User.objects.create_user(
        username="admin",
        email="admin@test.com",
        password="password123"
    )

    refresh = RefreshToken.for_user(self.user)
    self.client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
    )

    self.employee = Employee.objects.create(
        name="Adam",
        email="adam@test.com",
        department="Engineering",
        role="Developer"
    )
  
  def test_create_employee(self):
    response = self.client.post('/api/employees/', {
      "name": "John",
      "email": "john@example.com",
      "department": "HR",
      "role": "Manager"
    })
    self.assertEqual(response.status_code, 201)
  
  def test_create_employee_duplicate_email(self):
    response = self.client.post('/api/employees/', {
        "name": "Someone",
        "email": "adam@test.com"
    })
    self.assertEqual(response.status_code, 400)

  def test_create_employee_empty_name(self):
    response = self.client.post('/api/employees/', {
        "name": "",
        "email": "empty@test.com"
    })
    self.assertEqual(response.status_code, 400)










