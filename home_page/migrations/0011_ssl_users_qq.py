# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0010_ssl_table_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssl_users',
            name='qq',
            field=models.IntegerField(default=0, verbose_name=b'qq'),
            preserve_default=True,
        ),
    ]
