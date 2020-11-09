from django.db import models
from reads.models import Article


class FirebaseUser(models.Model):
    username = models.CharField(max_length=100)
    uid = models.CharField(max_length=128, unique=True)
    favourites = models.ManyToManyField(Article)
