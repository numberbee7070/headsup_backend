from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed

from .permissions import FirebaseAuthPermission
from .serializers import FirebaseUserInfoSerializer, FirebaseUserSerializer, FirebaseUserRenameSerializer
from .utils import CSRFExemptMixin


class NewUserView(CSRFExemptMixin, generics.CreateAPIView):
    serializer_class = FirebaseUserSerializer


class UserInfoView(CSRFExemptMixin, generics.RetrieveAPIView):
    serializer_class = FirebaseUserInfoSerializer
    permission_classes = (FirebaseAuthPermission,)

    def get_object(self):
        return self.request.firebase_user


class UserRenameView(CSRFExemptMixin, generics.UpdateAPIView):
    serializer_class = FirebaseUserRenameSerializer
    permission_classes = (FirebaseAuthPermission,)

    def get_object(self):
        return self.request.firebase_user
