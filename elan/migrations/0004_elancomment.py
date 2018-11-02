# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elan', '0003_auto_20181024_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElanComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Ad')),
                ('comment', models.TextField(verbose_name=b'Yorum')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('elan', models.ForeignKey(related_name='elancomments', to='elan.Elan')),
            ],
        ),
    ]
