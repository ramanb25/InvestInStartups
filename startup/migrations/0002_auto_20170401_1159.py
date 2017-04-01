# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 11:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='startup',
        ),
        migrations.AddField(
            model_name='startupprofile',
            name='shareCount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startupprofile',
            name='sharePrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startupprofile',
            name='stockName',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='stocks',
        ),
    ]