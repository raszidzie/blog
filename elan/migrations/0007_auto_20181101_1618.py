# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('elan', '0006_elan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='elan',
            name='ownerCity',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='elan',
            name='user',
            field=models.ForeignKey(related_name='elans', to=settings.AUTH_USER_MODEL),
        ),
    ]
