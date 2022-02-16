from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField(blank=True, null=True)
    poster = models.CharField(max_length=2083)
    genres = models.TextField(blank=True, null=True)
