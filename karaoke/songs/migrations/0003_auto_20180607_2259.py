# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-07 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20180607_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Artiste',
        ),
    ]
