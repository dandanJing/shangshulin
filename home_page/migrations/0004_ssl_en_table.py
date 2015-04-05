# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_ssl_table_itemcostprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ssl_en_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemid', models.CharField(max_length=100, verbose_name=b'itemId')),
                ('itemname', models.CharField(max_length=100, verbose_name=b'itemName')),
                ('itemcostprice', models.IntegerField(verbose_name=b'itemCostPrice')),
                ('itemprice', models.IntegerField(verbose_name=b'itemPrice')),
                ('itemsnum', models.IntegerField(verbose_name=b'itemsNum')),
                ('itemimageurl', models.CharField(max_length=200, verbose_name=b'itemImageUrl')),
                ('itemimagetable', models.CharField(max_length=100, verbose_name=b'itemImageTable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
