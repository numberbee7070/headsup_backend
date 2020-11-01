from rest_framework import permissions


class FirebaseAuthPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'firebase_user')
