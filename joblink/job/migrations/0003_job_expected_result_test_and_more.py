# Generated by Django 4.1.2 on 2022-11-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0002_joblocation_company_jobskill_jobcategory_job"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="expected_result_test",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="limited_day_confirm_schedule",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="limited_day_do_test",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]