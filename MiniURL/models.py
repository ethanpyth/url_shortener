from django.db import models

# Create your models here.


class MiniURL(models.Model):
    long_url = models.URLField(unique=True)
    code = models.CharField(max_length=10, unique=True)
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    pseudo = models.CharField(max_length=255, blank=True, null=True)
    nbre_access = models.IntegerField(default=0)
