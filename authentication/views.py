from rest_framework import generics
from rest_framework.response import Response
from .serializers import NewFirebaseUserSerializer


class NewUserView(generics.CreateAPIView):
    serializer_class = NewFirebaseUserSerializer
