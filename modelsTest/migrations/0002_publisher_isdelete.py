# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-05 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
