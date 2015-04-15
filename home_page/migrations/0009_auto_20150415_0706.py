# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0008_auto_20150415_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ssl_table',
            name='sellerName',
        ),
        migrations.AddField(
            model_name='ssl_table',
            name='username',
            field=models.CharField(default=b'\xe5\xb0\x9a\xe4\xb9\xa6\xe6\x9e\x97', max_length=100, verbose_name=b'username'),
            preserve_default=True,
        ),
    ]
