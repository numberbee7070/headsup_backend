from firebase_admin.auth import (InvalidIdTokenError, RevokedIdTokenError,
                                 verify_id_token)
from rest_framework import serializers, status

from .models import FirebaseUser


class FirebaseUserSerializer(serializers.Serializer):
    idtoken = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=100)
    favourites = serializers.ListField(read_only=True)

    def validate_idtoken(self, value):
        try:
            uid = verify_id_token(value)["uid"]
        except ValueError:
            raise serializers.ValidationError(
                "Not a valid type", code="invalid-idtoken-type")
        except InvalidIdTokenError:
            raise serializers.ValidationError(
                "Invalid id token", code="invalid-idtoken")

        # pylint: disable=no-member
        if FirebaseUser.objects.filter(uid=uid).exists():
            raise serializers.ValidationError(
                "User already exists", code="user-already-exists")
        return uid

    def create(self, validated_data):
        print(validated_data)

        # pylint: disable=no-member
        return FirebaseUser.objects.create(
            username=validated_data["username"],
            uid=validated_data["idtoken"]
        )
