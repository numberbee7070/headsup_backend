from authentication.permissions import FirebaseAuthPermission
from authentication.utils import get_firebase_user
from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .models import DiaryEntry
from .serializers import DiarySerializer


class DiaryListCreateView(generics.ListCreateAPIView):
    serializer_class = DiarySerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    permission_classes = (FirebaseAuthPermission,)

    def perform_create(self, serializer):
        user = get_firebase_user(self.request)
        serializer.save(user=user)

    def get_queryset(self):
        user = get_firebase_user(self.request)
        # pylint: disable=no-member
        return DiaryEntry.objects.filter(user=user)
