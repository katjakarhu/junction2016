# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hapiapp', '0002_fakesite'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakesite',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='fakesite',
            name='sourcename',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='fakesite',
            name='sourceurl',
            field=models.CharField(default='', max_length=255),
        ),
    ]
