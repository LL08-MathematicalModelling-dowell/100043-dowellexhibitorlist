# Generated by Django 3.1.2 on 2021-09-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('brand_name', models.CharField(max_length=256)),
                ('name_incharge', models.CharField(max_length=256)),
                ('designation_incharge', models.CharField(max_length=500)),
                ('exhibitor_page_link', models.URLField(blank=True, max_length=2048, null=True)),
                ('exhibitor_website', models.URLField(max_length=2048)),
                ('exhibitor_email', models.EmailField(max_length=256)),
                ('exhibitor_both_number', models.CharField(max_length=500)),
                ('exhibitor_city', models.CharField(max_length=500)),
                ('exhibitor_country', models.CharField(max_length=500)),
                ('exhibitor_address', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=50)),
                ('exhibitor_product', models.CharField(max_length=500)),
                ('linkedin', models.URLField(blank=True, max_length=2048, null=True)),
                ('twitter', models.URLField(blank=True, max_length=2048, null=True)),
                ('facebook', models.URLField(blank=True, max_length=2048, null=True)),
                ('instagram', models.URLField(blank=True, max_length=2048, null=True)),
                ('youtube', models.URLField(blank=True, max_length=2048, null=True)),
                ('tiktok', models.URLField(blank=True, max_length=2048, null=True)),
                ('hashtag', models.CharField(max_length=256)),
                ('mention', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=1000)),
                ('logo', models.ImageField(blank=True, upload_to='exhibitors/')),
            ],
        ),
    ]
