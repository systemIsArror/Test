# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-05 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0002_publisher_isdelete'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='publisher',
            managers=[
                ('pub', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='publisher',
            name='pub_price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=5),
        ),
    ]
