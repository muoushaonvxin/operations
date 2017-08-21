# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 00:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordCrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ssh_crack_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50, verbose_name='破解的密码')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.host')),
            ],
        ),
    ]