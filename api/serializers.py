from rest_framework import serializers

from .models import Employee, Client


class EmployeeStatisticsSerializer(serializers.ModelSerializer):
    total_sales_amount = serializers.FloatField()
    total_unique_clients = serializers.IntegerField()
    total_items_sold = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = [
            "id",
            "full_name",
            "birthdate",
            "total_sales_amount",
            "total_unique_clients",
            "total_items_sold",
        ]


class ClientStatisticsSerializer(serializers.ModelSerializer):
    total_sales_amount = serializers.FloatField()
    total_items_purchased = serializers.IntegerField()

    class Meta:
        model = Client
        fields = [
            "id",
            "full_name",
            "birthdate",
            "total_sales_amount",
            "total_items_purchased",
        ]
