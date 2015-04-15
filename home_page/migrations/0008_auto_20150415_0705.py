# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_auto_20150414_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='ssl_images_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemid', models.CharField(max_length=100, verbose_name=b'itemId')),
                ('itemimageurl', models.CharField(max_length=200, verbose_name=b'itemImageUrl')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ssl_table',
            name='itemimagetable',
        ),
        migrations.AddField(
            model_name='ssl_table',
            name='isBlock',
            field=models.IntegerField(default=0, verbose_name=b'isBlock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ssl_table',
            name='lastEditTime',
            field=models.IntegerField(default=0, verbose_name=b'lastEditTime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ssl_table',
            name='lookCount',
            field=models.IntegerField(default=0, verbose_name=b'lookCount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ssl_table',
            name='postTime',
            field=models.IntegerField(default=0, verbose_name=b'postTime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ssl_table',
            name='sellerName',
            field=models.CharField(default=b'\xe5\xb0\x9a\xe4\xb9\xa6\xe6\x9e\x97', max_length=100, verbose_name=b'sellerName'),
            preserve_default=True,
        ),
    ]
