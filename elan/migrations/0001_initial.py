# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('elanTitle', models.CharField(max_length=200)),
                ('elanDescription', models.CharField(max_length=200)),
                ('elanPrice', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]
