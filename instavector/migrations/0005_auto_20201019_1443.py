# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 11:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instavector', '0004_auto_20201019_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='author',
        ),
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.ManyToManyField(blank=True, null='True', to=settings.AUTH_USER_MODEL),
        ),
    ]
