from django.contrib import admin

from .models import Client, Employee, Order, Product

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Order)
