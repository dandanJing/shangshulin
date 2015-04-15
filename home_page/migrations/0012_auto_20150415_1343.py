# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0011_ssl_users_qq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssl_table',
            name='isBlock',
            field=models.BooleanField(default=True, verbose_name=b'isBlock'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ssl_table',
            name='lastEditTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 15, 13, 43, 45, 960026), verbose_name=b'lastEditTime'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ssl_table',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 15, 13, 43, 45, 959955), verbose_name=b'postTime'),
            preserve_default=True,
        ),
    ]
