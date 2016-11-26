from django.db import models
from django.utils import timezone

class FakeSite(models.Model):
    site = models.CharField(max_length=255)
    sourceurl = models.CharField(max_length=255, default='')
    sourcename = models.CharField(max_length=255, default = '')
    created = models.DateTimeField(default=timezone.now)

class FakeNews(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    isFake = models.BooleanField()
