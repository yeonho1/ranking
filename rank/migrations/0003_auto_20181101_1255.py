# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-01 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0002_auto_20181101_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranker',
            name='additions',
            field=models.CharField(default='\uc5c6\uc74c', max_length=255, verbose_name='\ube44\uace0'),
        ),
    ]