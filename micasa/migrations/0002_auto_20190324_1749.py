# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-24 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micasa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
    ]
