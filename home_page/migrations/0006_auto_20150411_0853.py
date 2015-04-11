# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0005_ssl_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssl_users',
            name='mobilephone',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'mobilephone'),
            preserve_default=True,
        ),
    ]
