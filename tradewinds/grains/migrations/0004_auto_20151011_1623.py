# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grains', '0003_auto_20150930_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='owner',
            new_name='company',
        ),
        migrations.AddField(
            model_name='account',
            name='person',
            field=models.ForeignKey(to='grains.Person', null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='userId',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='userId',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
