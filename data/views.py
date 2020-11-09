from authentication.permissions import FirebaseAuthPermission
from authentication.utils import CSRFExemptMixin
from rest_framework import generics

from .models import DiaryEntry
from .serializers import DiarySerializer


class DiaryListCreateView(CSRFExemptMixin, generics.ListCreateAPIView):
    serializer_class = DiarySerializer
    permission_classes = (FirebaseAuthPermission,)

    def perform_create(self, serializer):
        user = self.request.firebase_user
        serializer.save(user=user)

    def get_queryset(self):
        user = self.request.firebase_user
        # pylint: disable=no-member
        return DiaryEntry.objects.filter(user=user)
