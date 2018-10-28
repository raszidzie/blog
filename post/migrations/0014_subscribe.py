# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20181023_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=100)),
            ],
        ),
    ]
