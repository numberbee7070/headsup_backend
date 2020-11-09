from authentication.permissions import FirebaseAuthPermission
from authentication.serializers import FirebaseUserInfoSerializer
from authentication.utils import CSRFExemptMixin
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer, ListArticleSerializer


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


class ArticleFavouriteView(APIView):
    permission_classes = (FirebaseAuthPermission, )

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        request.firebase_user.favourites.add(article)
        return Response(FirebaseUserInfoSerializer(request.firebase_user).data)

    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        request.firebase_user.remove(article)
        return Response(FirebaseUserInfoSerializer(request.firebase_user).data)
