from datetime import date
from django.test import TestCase

from api.models import Order, Client, Employee, Product


class ModelTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            full_name="Test Client", birthdate="1990-01-01"
        )
        self.employee = Employee.objects.create(
            full_name="Test Employee", birthdate="1985-05-05"
        )
        self.product = Product.objects.create(
            name="Test Product", quantity=100, price=10.0
        )

        self.order = Order.objects.create(
            client=self.client,
            employee=self.employee,
            price=10.0,
            date=date.today(),
        )
        self.order.products.add(self.product)

    def test_order_model(self):
        self.assertEqual(self.order.client.full_name, "Test Client")
        self.assertEqual(self.order.employee.full_name, "Test Employee")
        self.assertEqual(self.order.products.first().name, "Test Product")
        self.assertEqual(self.order.price, 10.0)
        self.assertIsNotNone(self.order.date)

    def test_client_model(self):
        self.assertEqual(self.client.full_name, "Test Client")

    def test_employee_model(self):
        self.assertEqual(self.employee.full_name, "Test Employee")

    def test_product_model(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.quantity, 100)
        self.assertEqual(self.product.price, 10.0)
