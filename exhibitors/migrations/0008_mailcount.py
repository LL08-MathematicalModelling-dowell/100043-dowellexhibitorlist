# Generated by Django 3.1.2 on 2022-04-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('exhibitors', '0007_exhibitor_bdeventid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]
