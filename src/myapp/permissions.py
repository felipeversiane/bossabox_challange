from rest_framework import permissions
from django.contrib.auth.models import User


class StafflistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.META)
        user = User.objects.filter(username=request.user).first()
        if user:
            return user.is_staff
        else:
         return False
