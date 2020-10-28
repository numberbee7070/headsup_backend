from .models import FirebaseUser
from firebase_admin.auth import verify_id_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def get_firebase_user(request):
    token = request.META['HTTP_AUTHORIZATION'].split(' ')[-1]
    uid = verify_id_token(token)['uid']
    # pylint: disable=no-member
    return FirebaseUser.objects.get(uid=uid)


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dipatch(self, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)
