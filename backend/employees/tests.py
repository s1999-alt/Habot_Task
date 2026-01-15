from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Employee


class EmployeeTests(APITestCase):

  def test_create_employee(self):
    data = {
      "name": "adam",
      "email": "adam@example.com"
    }
    response = self.client.post('api/employees/', data)
    self.assertEqual(response.status_code, 201)
  
  def test_duplicate_email(self):
    Employee.objects.create(name="A", email="a@test.com")
    response = self.client.post('/api/employees/', {
      "name": "B",
      "email": "a@test.com"
    })
    self.assertEqual(response.status_code, 400)








