# Generated by Django 3.1.2 on 2021-10-05 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0002_auto_20210930_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='exhibitors_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999),
                                                  django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='details',
            name='visitors_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999),
                                                  django.core.validators.MinValueValidator(1)]),
        ),
    ]
