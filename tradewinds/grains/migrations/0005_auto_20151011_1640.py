# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grains', '0004_auto_20151011_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounttype',
            name='firmId',
        ),
        migrations.AddField(
            model_name='accounttype',
            name='userId',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
