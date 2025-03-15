from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.Employees.as_view(), name = "employees_details"),
    path("employees/<int:pk>/", views.Employees.as_view(), name = "employees_details"),
]