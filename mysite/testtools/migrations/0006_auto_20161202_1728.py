# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtools', '0005_auto_20161130_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testscenarios',
            name='interface_mapping_result',
        ),
        migrations.AddField(
            model_name='testscenarios',
            name='interfaces',
            field=models.ManyToManyField(to='testtools.Interface'),
        ),
        migrations.AlterField(
            model_name='requestparam',
            name='request_param_value',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'\xe8\xaf\xb7\xe6\xb1\x82\xe5\x8f\x82\xe6\x95\xb0\xe5\x80\xbc'),
        ),
    ]
