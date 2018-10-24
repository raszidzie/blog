# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20181023_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='person',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
