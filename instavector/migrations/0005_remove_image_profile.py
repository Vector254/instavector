# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-18 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instavector', '0004_image_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]