from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .models import DiaryEntry
from authentication.permissions import FirebaseAuthPermission
from authentication.utils import get_firebase_user


class DiaryCreateListRetriveView(CreateModelMixin, RetrieveModelMixin,  ListModelMixin, GenericAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    permission_classes = (FirebaseAuthPermission,)

    def get_queryset(self):
        user = get_firebase_user(
            self.request.META['Authorization'].split(' ')[-1])
        # pylint: disable=no-member
        return DiaryEntry.objects.filter(user=user)
