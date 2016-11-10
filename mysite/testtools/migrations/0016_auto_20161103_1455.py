# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtools', '0015_auto_20161103_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestparam',
            name='request_desc',
        ),
        migrations.RemoveField(
            model_name='responseparam',
            name='response_desc',
        ),
        migrations.AddField(
            model_name='interface',
            name='request_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interface',
            name='response_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]