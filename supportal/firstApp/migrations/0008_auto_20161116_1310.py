# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0007_auto_20161116_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='identifier',
            field=models.CharField(default=None, max_length=40, unique=True),
        ),
    ]