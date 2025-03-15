from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.studentsApi, name = "studentsApi"),
    path('students/<int:pk>/', views.studentDetailsView, name="student_details"),

]