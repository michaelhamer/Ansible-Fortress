# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-04 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks', '0011_remove_playbook_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playbook',
            name='playbook_path',
            field=models.FilePathField(default='test.yml', match='*.yml', max_length=200, path='/etc/ansible/playbooks'),
        ),
    ]