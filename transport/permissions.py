from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'

class IsOrganizer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'organizer'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
