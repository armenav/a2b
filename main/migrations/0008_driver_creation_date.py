# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 17:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160311_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 11, 17, 20, 48, 662787)),
            preserve_default=False,
        ),
    ]
