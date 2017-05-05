# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inferno', '0006_auto_20170502_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='RankImageUpload',
            field=models.FileField(blank=True, upload_to='Inferno/static/images/Ranks'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='RankImage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]