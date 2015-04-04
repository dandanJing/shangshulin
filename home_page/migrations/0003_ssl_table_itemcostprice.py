# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_ssl_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssl_table',
            name='itemcostprice',
            field=models.IntegerField(default=0, verbose_name=b'itemCostPrice'),
            preserve_default=True,
        ),
    ]
