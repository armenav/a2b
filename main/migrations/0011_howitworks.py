# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_driver_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowItWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=700)),
            ],
            options={
                'verbose_name': 'How It Works',
                'verbose_name_plural': 'How It Workss',
            },
        ),
    ]
