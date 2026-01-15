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


  def test_list_employees(self):
    response = self.client.get('/api/employees/')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(len(response.data) >= 1)
  

  def test_filter_by_department(self):
    response = self.client.get('/api/employees/?department=Engineering')
    self.assertEqual(response.status_code, 200)

  def test_filter_by_role(self):
    response = self.client.get('/api/employees/?role=Developer')
    self.assertEqual(response.status_code, 200)
  

  def test_get_single_employee(self):
    response = self.client.get(f'/api/employees/{self.employee.id}/')
    self.assertEqual(response.status_code, 200)

  def test_get_invalid_employee(self):
    response = self.client.get('/api/employees/9999/')
    self.assertEqual(response.status_code, 404)

  
  def test_update_employee(self):
    response = self.client.put(
      f'/api/employees/{self.employee.id}/',
      {
        "name": "Adam Updated",
        "email": "adam@test.com",
        "department": "Engineering",
        "role": "Senior Developer"
      },
      format='json'
    )
    self.assertEqual(response.status_code, 200)

  
  def test_delete_employee(self):
    response = self.client.delete(f'/api/employees/{self.employee.id}/')
    self.assertEqual(response.status_code, 204)

  def test_delete_invalid_employee(self):
    response = self.client.delete('/api/employees/9999/')
    self.assertEqual(response.status_code, 404)


  def test_unauthenticated_access(self):
    self.client.credentials() 
    response = self.client.get('/api/employees/')
    self.assertEqual(response.status_code, 401)










