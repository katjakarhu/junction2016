from django.db import models

class FakeSite(models.Model):
    site = models.CharField(max_length=255)

class FakeNews(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    isFake = models.BooleanField()