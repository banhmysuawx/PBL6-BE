# Generated by Django 4.1.2 on 2022-11-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="limit_time_to_interview",
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
