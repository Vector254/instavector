# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-22 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instavector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to='instavector.Profile'),
        ),
    ]
