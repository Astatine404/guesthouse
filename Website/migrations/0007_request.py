# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0006_room_vip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.Person')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.Room')),
            ],
        ),
    ]
