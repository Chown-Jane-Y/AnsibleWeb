# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnsibleWebApp', '0007_auto_20161028_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='hostname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='servers',
            name='os',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='servers',
            name='type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
