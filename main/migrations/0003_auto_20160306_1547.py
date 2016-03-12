# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-06 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160302_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='fromwhere',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rides_from', to='main.City'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='passenger_number',
            field=models.IntegerField(blank=True, default=2),
        ),
        migrations.AlterField(
            model_name='ride',
            name='towhere',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rides_to', to='main.City'),
        ),
    ]