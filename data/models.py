from django.db import models
from authentication.models import FirebaseUser


def diary_photo_path(instance, filename):
    return 'u%d/%s' % (instance.user.id, filename)


class DiaryEntry(models.Model):
    user = models.ForeignKey(FirebaseUser, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=diary_photo_path)


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    audio = models.FileField(upload_to='articles/audio')
    image = models.ImageField(upload_to='articles/image')
