# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 23:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_migrate_to_pinax_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='primary_image',
        ),
    ]
