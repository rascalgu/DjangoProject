# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-01 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('blog_body', models.TextField()),
                ('blog_type', models.CharField(max_length=50)),
                ('blog_timestamp', models.DateTimeField()),
                ('blog_imgurl', models.CharField(max_length=200, null=True)),
                ('blog_author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_id', models.IntegerField(default=0)),
                ('tree_pid', models.IntegerField(default=0)),
                ('tree_name', models.CharField(max_length=200)),
                ('intf_name', models.CharField(max_length=50)),
                ('intf_type', models.CharField(max_length=10)),
                ('intf_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Intf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_sn', models.CharField(max_length=10)),
                ('interface_name', models.CharField(max_length=80)),
                ('request_method', models.CharField(max_length=10)),
                ('request_link', models.CharField(max_length=255)),
                ('interface_desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('work', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
