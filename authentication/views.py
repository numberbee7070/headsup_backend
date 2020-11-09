from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed

from .permissions import FirebaseAuthPermission
from .serializers import FirebaseUserSerializer, FirebaseUserInfoSerializer
from .utils import CSRFExemptMixin


class NewUserView(CSRFExemptMixin, generics.CreateAPIView):
    serializer_class = FirebaseUserSerializer


class UserView(CSRFExemptMixin, generics.RetrieveAPIView):
    serializer_class = FirebaseUserInfoSerializer
    permission_classes = (FirebaseAuthPermission,)

    def get_object(self):
        return self.request.firebase_user
