# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('email', models.EmailField(max_length=200, verbose_name='邮箱')),
                ('message', models.TextField(verbose_name='留言')),
                ('active', models.BooleanField(default=True, verbose_name='有效')),
                ('posted', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
    ]
