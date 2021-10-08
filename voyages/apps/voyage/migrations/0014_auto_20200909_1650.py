# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-09 16:50
from __future__ import unicode_literals

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0013_auto_20200909_1533'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='voyage',
            managers=[
                ('all_dataset_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='voyage',
            name='dataset',
            field=models.IntegerField(
                default=0,
                help_text='Which dataset the voyage belongs to '
                          '(e.g. Transatlantic, IntraAmerican)'
            ),
        ),
        # Set dataset for intra American voyages.
        migrations.RunSQL(
            ['UPDATE voyage_voyage SET dataset=1 WHERE is_intra_american=1'],
            reverse_sql=[
                'UPDATE voyage_voyage SET is_intra_american=1 WHERE dataset=1'
            ]),
        migrations.RemoveField(
            model_name='voyage',
            name='is_intra_american',
        ),
    ]
