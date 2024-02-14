from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Employee, Client, Product, Order


class MyAPITestCase(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            full_name="John Doe", birthdate="1990-01-01"
        )
        self.client = Client.objects.create(
            full_name="Alice Smith", birthdate="1985-05-05"
        )
        self.product = Product.objects.create(
            name="Medical Device", quantity=10, price=100.0
        )
        self.order = Order.objects.create(
            client=self.client, employee=self.employee, price=100.0, date="2023-01-01"
        )

    def test_employee_statistics_api(self):
        response = self.client.get(
            f"/api/v1/statistics/employee/{self.employee.id}/?month=1&year=2023"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["full_name"], "John Doe")

    def test_employee_list_statistics_api(self):
        response = self.client.get("/api/v1/statistics/employee/?month=1&year=2023")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_client_statistics_api(self):
        response = self.client.get(
            f"/api/v1/statistics/client/{self.client.id}/?month=1&year=2023"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["full_name"], "Alice Smith")
