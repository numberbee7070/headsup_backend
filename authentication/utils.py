from .models import FirebaseUser
from firebase_admin.auth import verify_id_token


def get_firebase_user(token):
    uid = verify_id_token(token)['uid']
    # pylint: disable=no-member
    return FirebaseUser.objects.get(uid=uid)
