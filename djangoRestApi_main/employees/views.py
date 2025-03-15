from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from employees.permissions import  DeleteExistsPermission
from django.http import Http404

# Create your views here.
class Employees(APIView):
   def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
   
   def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([DeleteExistsPermission])
class EmployeesUpdate(APIView):
    def get_object(self, pk): 
       try:
          print(f"Fetching Employee with ID: {pk}")  # 👈 Debugging ke liye
          return Employee.objects.get(pk=pk)
       except Employee.DoesNotExist:
          print("Employee not found")  # 👈 Debugging ke liye
          raise Http404("Employee not found")

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
       employee = self.get_object(pk)
       employee.delete()
       return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)