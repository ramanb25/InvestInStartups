# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0002_auto_20170403_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='startupprofile',
            name='bank',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startupprofile',
            name='ifsc',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]
