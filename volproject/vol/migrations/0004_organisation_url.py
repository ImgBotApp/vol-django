# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vol', '0003_job_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='url',
            field=models.CharField(default='http://localhost', max_length=200),
            preserve_default=False,
        ),
    ]
