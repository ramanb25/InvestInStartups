# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 09:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inv',
            new_name='InvestorProfile',
        ),
    ]