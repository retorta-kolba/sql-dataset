# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20171207_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScienceField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='sciencefield',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='data.DataSource'),
            preserve_default=False,
        ),
    ]
