from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()

    def __str__(self):
        return self.full_name


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.client.full_name} - {self.date}"
