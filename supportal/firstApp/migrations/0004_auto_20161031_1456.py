# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_issue_highpriority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(help_text='Give a description of your issue.'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='title',
            field=models.CharField(help_text='Give a title for your issue.', max_length=120),
        ),
    ]
