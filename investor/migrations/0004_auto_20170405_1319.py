# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('investor', '0003_auto_20170405_1305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='investorprofile',
            unique_together=set([('accno', 'ifsc', 'bank')]),
        ),
    ]
