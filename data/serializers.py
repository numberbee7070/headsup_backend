from rest_framework import serializers

from .models import DiaryEntry, Article


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = ('content', 'image', 'created')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ListArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'image')
