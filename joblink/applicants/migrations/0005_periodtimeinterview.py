# Generated by Django 4.1.2 on 2022-12-01 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "applicants",
            "0004_applicantinterview_choice_set_schedule_interview_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="PeriodTimeInterview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                (
                    "applicant_interview",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="period_times",
                        to="applicants.applicantinterview",
                    ),
                ),
            ],
            options={
                "db_table": "period_time_interview",
            },
        ),
    ]
