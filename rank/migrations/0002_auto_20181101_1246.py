# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-01 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ranker',
            options={'verbose_name': 'Ranker', 'verbose_name_plural': 'Rankers'},
        ),
        migrations.AlterField(
            model_name='ranker',
            name='rank',
            field=models.IntegerField(verbose_name='\uc21c\uc704'),
        ),
    ]