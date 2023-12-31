# Generated by Django 4.1.10 on 2023-08-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events_venue", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="BDEventID",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="city",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="country",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="exhibitor",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="exhibitor_creator_list",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Complete", "Complete"),
                    ("InProgress", "InProgress"),
                    ("Error", "Error"),
                ],
                max_length=12,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="business_category",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="facebook",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="instagram",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="linkedin",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="logo",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="event",
            name="organiser_website",
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="tiktok",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="twitter",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="event",
            name="vanue_page_link",
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="event",
            name="website",
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="event",
            name="youtube",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]
