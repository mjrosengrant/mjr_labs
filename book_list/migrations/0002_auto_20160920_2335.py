# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-21 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='kit',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='kit',
            name='extra_content_type',
        ),
        migrations.RemoveField(
            model_name='kit',
            name='extra_object_id',
        ),
    ]