# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
