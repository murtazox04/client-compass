from django.urls import path
from .views import EmployeeStatistics, EmployeeListStatistics, ClientStatistics

urlpatterns = [
    path(
        "statistics/employee/<int:id>/",
        EmployeeStatistics.as_view(),
        name="employee_statistics",
    ),
    path(
        "employee/statistics/",
        EmployeeListStatistics.as_view(),
        name="employee_list_statistics",
    ),
    path(
        "statistics/client/<int:id>/",
        ClientStatistics.as_view(),
        name="client_statistics",
    ),
]
