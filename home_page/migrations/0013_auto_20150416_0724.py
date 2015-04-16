# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0012_auto_20150415_1343'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ssl_en_table',
        ),
        migrations.AddField(
            model_name='ssl_table',
            name='itemType',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'itemType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ssl_table',
            name='lastEditTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 7, 24, 26, 192365), verbose_name=b'lastEditTime'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ssl_table',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 7, 24, 26, 192221), verbose_name=b'postTime'),
            preserve_default=True,
        ),
    ]
