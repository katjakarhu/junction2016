# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hapiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255)),
            ],
        ),
    ]
