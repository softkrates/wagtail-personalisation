# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalisation', '0006_visitcountrule'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitcountrule',
            name='count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitcountrule',
            name='operator',
            field=models.CharField(choices=[('more_than', 'More than'), ('less_than', 'Less than'), ('equal_to', 'Equal to')], default='ht', max_length=20),
        ),
    ]