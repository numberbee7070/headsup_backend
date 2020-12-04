from authentication.permissions import FirebaseAuthPermission
from authentication.utils import CSRFExemptMixin
from django.conf import settings
from rest_framework import generics

from .models import DiaryEntry
from .serializers import DiarySerializer


class DiaryListCreateView(CSRFExemptMixin, generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = DiarySerializer
    permission_classes = (FirebaseAuthPermission,)

    def perform_create(self, serializer):
        user = self.request.firebase_user
        serializer.save(user=user)

    def get_queryset(self):
        # pylint: disable=no-member
        # access all when debug True
        if settings.DEBUG:
            return DiaryEntry.objects.order_by('-created')
        user = self.request.firebase_user
        return DiaryEntry.objects.filter(user=user).order_by('-created')
