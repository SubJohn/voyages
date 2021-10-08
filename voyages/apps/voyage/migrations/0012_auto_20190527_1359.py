# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-27 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0011_auto_20181025_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='child_ratio_among_embarked_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Child ratio among embarked slaves (CHILRAT1)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='child_ratio_among_landed_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Child ratio among landed slaves (CHILRAT3)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='male_ratio_among_embarked_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Male ratio among embarked slaves (MALRAT1)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='male_ratio_among_landed_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Male ratio among landed slaves (MALRAT3)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_boys_among_embarked_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of boys '
                             'among embarked slaves (BOYRAT1)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_boys_among_landed_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of boys '
                             'among landed slaves (BOYRAT3)'
            ),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_girls_among_embarked_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of girls '
                             'among embarked slaves (GIRLRAT1)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_girls_among_landed_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of girls '
                             'among landed slaves (GIRLRAT3)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_men_among_embarked_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of men '
                             'among embarked slaves (MENRAT1)'
            ),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_men_among_landed_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of men among landed slaves (MENRAT3)'
            ),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_women_among_embarked_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of women '
                             'among embarked slaves (WOMRAT1)'),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='percentage_women_among_landed_slaves',
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name='Percentage of women '
                             'among landed slaves (WOMRAT3)'
            ),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='total_slaves_by_age_gender_identified_among_landed',
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name='Total slaves identified by age and gender '
                             'among landed (SLAVMAX3)'
            ),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='total_slaves_by_age_gender_identified_departure_or_arrival',
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name='Total slaves identified by age and gender '
                             'at departure or arrival (SLAVMAX7)'
            ),
        ),
        migrations.AddField(
            model_name='voyageslavesnumbers',
            name='total_slaves_embarked_age_gender_identified',
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name='Total slaves embarked with age and gender '
                             'identified (SLAVMAX1)'
            ),
        ),
    ]
