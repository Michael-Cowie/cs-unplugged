# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0093_auto_20171026_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='agegroup',
            name='description_de',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='agegroup',
            name='description_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='agegroup',
            name='description_fr',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
