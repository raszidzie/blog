# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elan',
            name='ownerMail',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='elan',
            name='ownerPhone',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
