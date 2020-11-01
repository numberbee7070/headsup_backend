from authentication.permissions import FirebaseAuthPermission
from rest_framework import generics

from .models import Article, DiaryEntry
from .serializers import (ArticleSerializer, DiarySerializer,
                          ListArticleSerializer)

from authentication.utils import CSRFExemptMixin


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


class ListArticleView(CSRFExemptMixin, generics.ListAPIView):
    permission_classes = (FirebaseAuthPermission,)
    serializer_class = ListArticleSerializer
    # pylint: disable=no-member
    queryset = Article.objects.all()


class RetrieveArticleView(CSRFExemptMixin, generics.RetrieveAPIView):
    permission_classes = (FirebaseAuthPermission,)
    serializer_class = ArticleSerializer
    # pylint: disable=no-member
    queryset = Article.objects.all()
