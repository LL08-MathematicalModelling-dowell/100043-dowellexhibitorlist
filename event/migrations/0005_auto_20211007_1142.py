# Generated by Django 3.1.2 on 2021-10-07 11:42

import djongo.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0004_auto_20211007_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='logo',
            field=models.ImageField(
                storage=djongo.storage.GridFSStorage(base_url='form.urlsmedia/', collection='event'), upload_to=''),
        ),
    ]
