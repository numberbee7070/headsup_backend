from django.conf import settings
from firebase_admin.auth import (InvalidIdTokenError, RevokedIdTokenError,
                                 get_user, verify_id_token)
from rest_framework import serializers, status

from .models import FirebaseUser


class FirebaseUserSerializer(serializers.Serializer):
    idtoken = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=100)

    def validate_idtoken(self, value):
        # for debugging
        if settings.DEBUG:
            return value

        try:
            uid = verify_id_token(value)["uid"]
        except ValueError:
            raise serializers.ValidationError(
                "Not a valid type", code="invalid-idtoken-type")
        except InvalidIdTokenError:
            raise serializers.ValidationError(
                "Invalid id token", code="invalid-idtoken")

        user_record = get_user(uid)
        if user_record.email and not user_record.email_verified:
            raise serializers.ValidationError(
                "user not verified", code="user-not-verified")

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


class FirebaseUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseUser
        fields = ('username', 'favourites')


class FirebaseUserRenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseUser
        fields = ('username', )
