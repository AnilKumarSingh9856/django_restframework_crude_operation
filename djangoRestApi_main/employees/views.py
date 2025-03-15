from rest_framework.views import APIView
from  employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

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

   def delete(self, request, pk):
       employee = Employee.objects.get(pk=pk)
       employee.delete()
       return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
