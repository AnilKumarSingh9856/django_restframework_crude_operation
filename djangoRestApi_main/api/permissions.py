from rest_framework import permissions
from students.models import Student

class DeleteExistsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':   # DELETE request now allowed if student's data doesn't exist
            pk = view.kwargs.get("pk")   # Get student ID from URL
            return Student.objects.filter(pk=pk).exists()
        return True