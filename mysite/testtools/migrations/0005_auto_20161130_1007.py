# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 02:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testtools', '0004_auto_20161129_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interface',
            options={'ordering': ['interface_sn']},
        ),
        migrations.AlterModelOptions(
            name='testscenarios',
            options={'ordering': ['-createtime']},
        ),
    ]