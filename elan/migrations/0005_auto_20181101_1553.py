# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elan', '0004_elancomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elan',
            name='elanDescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='elancomment',
            name='elan',
            field=models.ForeignKey(related_name='comments', to='elan.Elan'),
        ),
    ]
