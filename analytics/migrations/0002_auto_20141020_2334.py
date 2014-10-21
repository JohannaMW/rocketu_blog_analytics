# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='view',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='ip_address',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='location',
            field=models.ForeignKey(blank=True, to='analytics.Location', null=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='page',
            field=models.ForeignKey(to='analytics.Page'),
        ),
    ]
