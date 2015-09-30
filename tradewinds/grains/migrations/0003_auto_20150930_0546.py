# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grains', '0002_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='creditAccount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='debitAccount',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(default=0, to='grains.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='txType',
            field=models.ForeignKey(default=0, to='grains.TransactionType'),
            preserve_default=False,
        ),
    ]
