# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onsale',
            old_name='user',
            new_name='owner',
        ),
    ]