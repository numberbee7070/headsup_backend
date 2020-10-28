from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed

from .permissions import FirebaseAuthPermission
from .serializers import FirebaseUserSerializer
from .utils import CSRFExemptMixin, get_firebase_user


class NewUserView(CSRFExemptMixin, generics.CreateAPIView):
    serializer_class = FirebaseUserSerializer


class UserView(CSRFExemptMixin, generics.RetrieveAPIView):
    serializer_class = FirebaseUserSerializer
    permission_classes = (FirebaseAuthPermission,)

    def get_object(self):
        try:
            token = self.request.META['HTTP_Authorization'].split(' ')[-1]
            return get_firebase_user(token)
        except Exception as e:
            print(e)
            raise AuthenticationFailed("authentication failed")
