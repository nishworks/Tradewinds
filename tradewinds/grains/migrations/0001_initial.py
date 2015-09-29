# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accountNumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('phoneNum', models.CharField(max_length=15)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firsName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('phoneNum', models.CharField(max_length=15)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='representative',
            field=models.ForeignKey(to='grains.Person'),
        ),
        migrations.AddField(
            model_name='accounttype',
            name='firmId',
            field=models.ForeignKey(to='grains.Firm'),
        ),
        migrations.AddField(
            model_name='account',
            name='accountType',
            field=models.ForeignKey(to='grains.AccountType'),
        ),
        migrations.AddField(
            model_name='account',
            name='firmId',
            field=models.ForeignKey(to='grains.Firm'),
        ),
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(to='grains.Company', null=True),
        ),
    ]
