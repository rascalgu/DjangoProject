# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtools', '0018_auto_20161111_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestScenarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_scenario_name', models.CharField(blank=True, max_length=200, null=True)),
                ('test_scenario_type', models.IntegerField()),
                ('interface_mapping_result', models.CharField(blank=True, max_length=200, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]