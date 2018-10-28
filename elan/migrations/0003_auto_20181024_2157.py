# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elan', '0002_auto_20181024_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='elan',
            name='image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='elan',
            name='itemCategory',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
