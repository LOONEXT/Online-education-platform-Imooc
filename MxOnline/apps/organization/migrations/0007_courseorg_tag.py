# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='全国知名', max_length=10, verbose_name='机构标签'),
        ),
    ]