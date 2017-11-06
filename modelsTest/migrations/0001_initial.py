# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-05 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='AuthorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelsTest.Author')),
            ],
            options={
                'db_table': 'authorinfo',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('publish_data', models.DateTimeField()),
                ('author', models.ManyToManyField(to='modelsTest.Author')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_name', models.CharField(max_length=100)),
                ('pub_address', models.CharField(max_length=100)),
                ('pub_city', models.CharField(max_length=50)),
                ('pub_province', models.CharField(max_length=100)),
                ('pub_website', models.URLField()),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelsTest.Publisher'),
        ),
    ]
