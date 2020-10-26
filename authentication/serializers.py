from rest_framework import serializers, status
from firebase_admin.auth import (verify_id_token, InvalidIdTokenError,
                                 RevokedIdTokenError, CertificateFetchError)
from .models import FirebaseUser


class NewFirebaseUserSerializer(serializers.Serializer):
    idtoken = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=100)

    def validate_idtoken(self, value):
        try:
            uid = verify_id_token(value)["uid"]
        except ValueError:
            raise serializers.ValidationError(
                "Not a valid type", code=status.HTTP_400_BAD_REQUEST)
        except InvalidIdTokenError:
            raise serializers.ValidationError(
                "Invalid id token", code=status.HTTP_401_UNAUTHORIZED)
        except CertificateFetchError:
            raise serializers.ValidationError(
                "Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # pylint: disable=no-member
        if FirebaseUser.objects.filter(uid=uid).exists():
            raise serializers.ValidationError(
                "user already exists", code=status.HTTP_409_CONFLICT)
        return uid

    def create(self, validated_data):
        print(validated_data)

        # pylint: disable=no-member
        return FirebaseUser.objects.create(
            username=validated_data["username"],
            uid=validated_data["idtoken"]
        )
