# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0013_auto_20150416_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssl_users',
            name='is_student',
            field=models.BooleanField(default=True, verbose_name=b'is_student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ssl_table',
            name='lastEditTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 11, 54, 53, 287309), verbose_name=b'lastEditTime'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ssl_table',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 11, 54, 53, 287256), verbose_name=b'postTime'),
            preserve_default=True,
        ),
    ]
