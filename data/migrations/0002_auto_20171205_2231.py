# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='lastupdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
