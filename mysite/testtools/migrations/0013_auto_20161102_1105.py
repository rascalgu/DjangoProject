# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtools', '0012_auto_20161102_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestparam',
            name='request_param_desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]