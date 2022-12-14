# Generated by Django 4.1.2 on 2022-11-24 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0006_alter_company_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobSkill",
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
                ("name", models.CharField(max_length=100)),
                ("level_name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_skills",
                        to="companies.company",
                    ),
                ),
            ],
            options={
                "db_table": "job_skills",
            },
        ),
        migrations.CreateModel(
            name="JobLocation",
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
                ("location_name", models.CharField(max_length=100)),
                (
                    "street_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(max_length=100)),
                ("zip", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_locations",
                        to="companies.company",
                    ),
                ),
            ],
            options={
                "db_table": "job_locations",
            },
        ),
        migrations.CreateModel(
            name="JobCategory",
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
                ("name", models.CharField(max_length=100)),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="companies.company",
                    ),
                ),
            ],
            options={
                "db_table": "job_categories",
            },
        ),
        migrations.CreateModel(
            name="Job",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("salary", models.CharField(blank=True, max_length=100, null=True)),
                ("is_company_name_hidden", models.BooleanField(default=True)),
                (
                    "limited_day_do_test",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "limited_day_confirm_schedule",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "expected_result_test",
                    models.FloatField(blank=True, default=0, null=True),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="job.jobcategory",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="companies.company",
                    ),
                ),
                (
                    "locations",
                    models.ManyToManyField(related_name="jobs", to="job.joblocation"),
                ),
                (
                    "skills",
                    models.ManyToManyField(related_name="jobs", to="job.jobskill"),
                ),
            ],
            options={
                "db_table": "jobs",
            },
        ),
    ]
