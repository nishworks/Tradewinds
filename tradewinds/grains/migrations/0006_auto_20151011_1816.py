# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grains', '0005_auto_20151011_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phoneNum',
        ),
        migrations.RemoveField(
            model_name='company',
            name='website',
        ),
    ]
