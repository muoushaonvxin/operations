# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 00:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.GenericIPAddressField(verbose_name='目标ip地址')),
                ('port', models.IntegerField(verbose_name='端口')),
                ('dictionary', models.CharField(max_length=32, verbose_name='字典名称')),
                ('user', models.CharField(default='root', max_length=32, verbose_name='用户')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='目标命名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
        ),
    ]
