from django.conf import settings
from rest_framework import permissions


class FirebaseAuthPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow all users when debug True
        return settings.DEBUG or hasattr(request, 'firebase_user')
