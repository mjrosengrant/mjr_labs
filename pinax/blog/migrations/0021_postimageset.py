# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.9.2 on 2017-11-12 21:44
=======
# Generated by Django 1.9.2 on 2017-11-12 22:01
>>>>>>> e02cdc2... Added .env file settings for database
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_images', '0001_initial'),
        ('blog', '0020_auto_20171106_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImageSet',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pinax_images.imageset',),
        ),
    ]
