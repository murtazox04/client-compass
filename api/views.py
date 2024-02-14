from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response

from .models import Employee, Client, Order
from .serializers import (
    EmployeeStatisticsSerializer,
    ClientStatisticsSerializer,
)


class EmployeeStatistics(generics.RetrieveAPIView):
    serializer_class = EmployeeStatisticsSerializer
    queryset = Employee.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        month = self.request.query_params.get("month")
        year = self.request.query_params.get("year")

        orders = Order.objects.filter(
            employee=instance, date__month=month, date__year=year
        )
        total_sales_amount = (
            orders.aggregate(total_sales_amount=Sum("price"))["total_sales_amount"] or 0
        )
        total_unique_clients = orders.values("client").distinct().count()
        total_items_sold = (
            orders.aggregate(total_items_sold=Sum("products__quantity"))[
                "total_items_sold"
            ]
            or 0
        )

        data = {
            "full_name": instance.full_name,
            "total_sales_amount": total_sales_amount,
            "total_unique_clients": total_unique_clients,
            "total_items_sold": total_items_sold,
        }
        return Response(data)


class EmployeeListStatistics(generics.ListAPIView):
    serializer_class = EmployeeStatisticsSerializer
    queryset = Employee.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for employee in queryset:
            orders = Order.objects.filter(
                employee=employee,
                date__month=self.request.query_params.get("month"),
                date__year=self.request.query_params.get("year"),
            )
            total_sales_amount = (
                orders.aggregate(total_sales_amount=Sum("price"))["total_sales_amount"]
                or 0
            )
            total_unique_clients = orders.values("client").distinct().count()
            total_items_sold = (
                orders.aggregate(total_items_sold=Sum("products__quantity"))[
                    "total_items_sold"
                ]
                or 0
            )
            employee_data = {
                "full_name": employee.full_name,
                "total_sales_amount": total_sales_amount,
                "total_unique_clients": total_unique_clients,
                "total_items_sold": total_items_sold,
            }
            data.append(employee_data)
        return Response(data)


class ClientStatistics(generics.RetrieveAPIView):
    serializer_class = ClientStatisticsSerializer
    queryset = Client.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        month = self.request.query_params.get("month")
        year = self.request.query_params.get("year")

        orders = Order.objects.filter(
            client=instance, date__month=month, date__year=year
        )
        total_sales_amount = (
            orders.aggregate(total_sales_amount=Sum("price"))["total_sales_amount"] or 0
        )
        total_items_purchased = (
            orders.aggregate(total_items_purchased=Sum("products__quantity"))[
                "total_items_purchased"
            ]
            or 0
        )

        data = {
            "full_name": instance.full_name,
            "total_sales_amount": total_sales_amount,
            "total_items_purchased": total_items_purchased,
        }
        return Response(data)
