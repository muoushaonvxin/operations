# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-15 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20171115_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='slot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='插槽位'),
        ),
    ]
