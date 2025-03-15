from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from employees.permissions import  DeleteExistsPermission
from django.http import Http404
from rest_framework import mixins, generics

# Create your views here.     
# class Employees(APIView):    # Class based views
#    def get(self, request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK) 
   
#    def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeesUpdate(APIView):
#     @permission_classes([DeleteExistsPermission])
#     def get_object(self, pk): 
#        try:
#           return Employee.objects.get(pk=pk)
#        except Employee.DoesNotExist:
#           raise Http404("Employee not found")

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#        employee = self.get_object(pk)
#        employee.delete()
#        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    

    def post(self, request):
        return self.create(request)

   

class EmployeesUpdate(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    @permission_classes([DeleteExistsPermission])   # used by my side in order to not show delete option when data in not present

    def get(self, request, pk):
        return self.retrieve(request, pk)
    

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)