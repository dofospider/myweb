# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='threeD',
            fields=[
                ('order', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('three_d', models.CharField(max_length=3)),
            ],
        ),
    ]