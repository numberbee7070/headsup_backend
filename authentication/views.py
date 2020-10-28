from rest_framework import generics
from rest_framework.response import Response
from .serializers import NewFirebaseUserSerializer
from .utils import CSRFExemptMixin


class NewUserView(CSRFExemptMixin, generics.CreateAPIView):
    serializer_class = NewFirebaseUserSerializer
