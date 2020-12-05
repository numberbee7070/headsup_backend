from rest_framework import serializers

from .models import DiaryEntry


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = ('id', 'content', 'image', 'created')
