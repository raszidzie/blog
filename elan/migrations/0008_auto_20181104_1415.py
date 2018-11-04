# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elan', '0007_auto_20181101_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elan',
            name='itemCategory',
            field=models.CharField(max_length=200, choices=[(b'work', b'WORK'), (b'kids', b'KIDS'), (b'services', b'SERVICES'), (b'education', b'EDUCATION'), (b'personal', b'PPERSONAL'), (b'apart', b'APART')]),
        ),
    ]
