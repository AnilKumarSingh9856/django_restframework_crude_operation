from django.urls import path
from .import views

urlpatterns = [
    path("", views.Employees.as_view(), name = "employees_list"),
    path("<int:pk>/", views.EmployeesUpdate.as_view(), name = "employees_details"),
]