from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    audio = models.FileField(upload_to='articles/audio')
    image = models.ImageField(upload_to='articles/image')
