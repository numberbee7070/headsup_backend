from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseServerError
from firebase_admin.auth import CertificateFetchError, verify_id_token

from .models import FirebaseUser


def firebase_auth_middleware(get_response):

    def debug(request):
        if 'Authorization' in request.headers:
            # pylint: disable=no-member
            request.firebase_user = FirebaseUser.objects.get(
                uid=request.headers['Authorization'])
        response = get_response(request)
        return response
    if settings.DEBUG:
        return debug

    def middleware(request):
        if 'Authorization' in request.headers:
            try:
                auth_header = request.headers["Authorization"]
                idtoken = auth_header.split(' ')[1]
                uid = verify_id_token(idtoken)["uid"]
                # pylint: disable=no-member
                request.firebase_user = FirebaseUser.objects.get(uid=uid)
            except CertificateFetchError:
                return HttpResponseServerError()
            except:
                return HttpResponseForbidden()
        response = get_response(request)

        return response

    return middleware
