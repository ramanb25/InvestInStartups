# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 19:16
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startupName', models.CharField(max_length=100)),
                ('stockName', models.CharField(max_length=100)),
                ('shareCount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('sharePrice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('aadhar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uid')),
                ('accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.accounts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
