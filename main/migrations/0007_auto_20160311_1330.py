# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160311_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
