# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instavector', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='name',
        ),
    ]
