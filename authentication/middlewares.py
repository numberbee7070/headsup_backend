from firebase_admin.auth import (verify_id_token, CertificateFetchError)
from .models import FirebaseUser
from django.http import HttpResponseServerError, HttpResponseForbidden


def firebase_auth_middleware(get_response):
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
