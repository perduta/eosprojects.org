# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_remove_timelineeventinserterrulebook_last'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelineeventinserterrulebook',
            name='last',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
