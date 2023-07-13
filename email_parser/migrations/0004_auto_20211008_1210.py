import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('email_parser', '0003_auto_20211007_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='BDEventID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='exhibitors_number',
            field=models.IntegerField(blank=True, null=True,
                                      validators=[django.core.validators.MaxValueValidator(99999),
                                                  django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='visitors_number',
            field=models.IntegerField(blank=True, null=True,
                                      validators=[django.core.validators.MaxValueValidator(99999),
                                                  django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
