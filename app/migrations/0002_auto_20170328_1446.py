# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inv',
            name='holdings',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inv',
            name='name',
            field=models.CharField(max_length=1),
        ),
    ]
