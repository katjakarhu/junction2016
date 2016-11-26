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

class SentimentData(models.Model):
    words = models.CharField(max_length=2048)
    url = models.CharField(max_length=255)
    containsHateSpeech = models.BooleanField()
    score = models.IntegerField(default=0)
    created =  models.DateTimeField(default=timezone.now)
