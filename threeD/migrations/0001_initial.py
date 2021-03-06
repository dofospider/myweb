# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='threeD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('order', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='threeDList',
            fields=[
                ('three_d', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('lost_count', models.IntegerField()),
                ('mix_repeat', models.IntegerField()),
                ('three_d_list', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='threed',
            name='td',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threeD.threeDList'),
        ),
    ]
