# Generated by Django 3.1.2 on 2021-09-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('exhibitors', '0003_auto_20210908_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitor',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
