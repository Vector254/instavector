# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-18 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instavector', '0007_auto_20201018_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='vector', on_delete=django.db.models.deletion.CASCADE, to='instavector.Profile'),
        ),
    ]