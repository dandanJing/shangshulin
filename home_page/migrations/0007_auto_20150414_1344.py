# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_auto_20150411_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssl_en_table',
            name='itemid',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'itemId'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ssl_table',
            name='itemid',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'itemId'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_items_table',
            name='userid',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'userId'),
            preserve_default=True,
        ),
    ]
