# Generated by Django 3.1.2 on 2021-11-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('exhibitors', '0006_auto_20211018_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='BDEventID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
