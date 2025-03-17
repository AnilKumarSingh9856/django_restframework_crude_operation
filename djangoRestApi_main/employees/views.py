from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from employees.permissions import  DeleteExistsPermission
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from blogs.paginations import CustomPagination
from employees.filters import EmployeeFilter

# Create your views here.  --> first way   
"""
class Employees(APIView):    # Class based views
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


class EmployeesUpdate(APIView):
    @permission_classes([DeleteExistsPermission])
    def get_object(self, pk): 
       try:
          return Employee.objects.get(pk=pk)
       except Employee.DoesNotExist:
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
"""


# Created class based views with the help of Mixing   --> Second way
"""
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
"""

# Created class based view with the help of genrics --> Third way
"""
class Employees(generics.ListCreateAPIView):  # Here combining the features of listing and creating data
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesUpdate(generics.RetrieveUpdateDestroyAPIView): # here combining the features of retrieving, updating, and deleting the data
    permission_classes = [DeleteExistsPermission]  # used by my side in order to not show delete option when data in not present
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
"""

# Created class based view  --> 4th way
"""
class EmployeeViewSet(viewsets.ViewSet):
    @permission_classes([DeleteExistsPermission])   # used by my side in order to not show delete option when data in not present
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset,  many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

# Created class based view  --> 5th way

class EmployeeViewSet(viewsets.ModelViewSet):   # only three line of code perform all the CRUD operation
    permission_classes = [DeleteExistsPermission] # used by my side in order to not show delete option when data in not present
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination     # using custom pagination
    # filterset_fields = ['designation']      # global filters and it is work for only individual field
    filterset_class = EmployeeFilter
    