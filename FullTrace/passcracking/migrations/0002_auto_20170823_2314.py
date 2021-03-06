# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 23:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
        ('passcracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ssh_crack_failed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.GenericIPAddressField(verbose_name='目标ip地址')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.host')),
            ],
        ),
        migrations.DeleteModel(
            name='PasswordCrack',
        ),
    ]
