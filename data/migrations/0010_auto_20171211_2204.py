# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20171211_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sciencefield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='data.ScienceField'),
        ),
    ]
