from rest_framework import permissions
from firebase_admin.auth import verify_id_token
from .models import FirebaseUser


class FirebaseAuthPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.META['Authorization'].split(' ')[-1]
        try:
            uid = verify_id_token(token)["uid"]
            # pylint: disable=no-member
            FirebaseUser.objects.get(uid=uid)
            return True
        except:
            return False
