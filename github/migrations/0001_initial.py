# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('repository_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('stars', models.IntegerField()),
                ('url', models.URLField()),
                ('created_date', models.DateTimeField()),
                ('last_pushed_date', models.DateTimeField()),
            ],
        ),
    ]
