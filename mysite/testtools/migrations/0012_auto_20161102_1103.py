# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtools', '0011_auto_20161102_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='response_param_desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]