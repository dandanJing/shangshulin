# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0009_auto_20150415_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssl_table',
            name='feature',
            field=models.CharField(default=b'\xe5\x85\xa8\xe6\x96\xb0', max_length=100, verbose_name=b'feature'),
            preserve_default=True,
        ),
    ]
