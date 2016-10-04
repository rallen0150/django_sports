# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=2)),
                ('points', models.FloatField()),
                ('rebounds', models.FloatField()),
                ('assists', models.FloatField()),
                ('steals', models.FloatField()),
                ('blocks', models.FloatField()),
                ('college', models.CharField(max_length=10)),

            ],
        ),
    ]