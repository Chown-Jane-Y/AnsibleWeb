# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnsibleWebApp', '0005_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]