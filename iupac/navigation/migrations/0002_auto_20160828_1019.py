# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottommenuitem',
            name='blank',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mainmenuitem',
            name='blank',
            field=models.BooleanField(default=False),
        ),
    ]
