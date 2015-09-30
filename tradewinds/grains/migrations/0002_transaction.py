# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firmId', models.CharField(max_length=150)),
                ('amount', models.IntegerField()),
                ('creditAccount', models.ForeignKey(related_name='credit', to='grains.Account')),
                ('debitAccount', models.ForeignKey(related_name='debit', to='grains.Account')),
            ],
        ),
    ]
