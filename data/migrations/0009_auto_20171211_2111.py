# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20171211_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sciencefield',
            name='metaid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
