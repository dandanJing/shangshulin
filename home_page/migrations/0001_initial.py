# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_items_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=50, verbose_name=b'userId')),
                ('userdisplayname', models.CharField(max_length=50, verbose_name=b'userDisplayName')),
                ('password', models.CharField(max_length=20, verbose_name=b'password')),
                ('realname', models.CharField(max_length=50, verbose_name=b'realName')),
                ('sex', models.CharField(max_length=10, verbose_name=b'sex')),
                ('email', models.EmailField(max_length=75, verbose_name=b'email', blank=True)),
                ('items_tablename', models.CharField(max_length=100, verbose_name=b'itemTableName')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
