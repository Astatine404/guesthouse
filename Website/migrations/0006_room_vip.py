# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0005_room_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='vip',
            field=models.BooleanField(default=False),
        ),
    ]
