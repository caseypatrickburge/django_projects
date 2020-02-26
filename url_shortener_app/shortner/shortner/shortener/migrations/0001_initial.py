# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-02-18 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shortner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputURL', models.CharField(max_length=64)),
                ('shortURL', models.CharField(max_length=12)),
                ('ip', models.CharField(max_length=16)),
                ('redirect', models.CharField(max_length=16)),
                ('url_bits', models.IntegerField(default=0)),
            ],
        ),
    ]