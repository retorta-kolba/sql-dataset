# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20171207_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='url',
            field=models.URLField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
