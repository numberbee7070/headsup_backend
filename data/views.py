from authentication.permissions import FirebaseAuthPermission
from authentication.utils import get_firebase_user
from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from django.views import View
from django.http import JsonResponse

from .models import DiaryEntry
from .serializers import DiarySerializer
import pymongo


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


def article_view(request, chapter=None):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    collection = client.test.Reads
    if chapter:
        data = collection.find_one({"chapter": chapter}, {"_id": False})
        return JsonResponse(data)
    data = collection.find(
        projection={'_id': False,
                    'chapter': True,
                    "body": {"title": True}
                    }
    )
    return JsonResponse(list(data), safe=False)
