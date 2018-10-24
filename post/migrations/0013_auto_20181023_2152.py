# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20181023_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=b'200', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
