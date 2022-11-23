# Generated by Django 4.1.2 on 2022-11-16 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("fullname", models.CharField(blank=True, default="", max_length=256)),
                ("email", models.EmailField(blank=True, default="", max_length=256)),
                ("cv", models.FileField(blank=True, default=None, upload_to="")),
                (
                    "cover_letter",
                    models.TextField(blank=True, default="", max_length=500),
                ),
                ("status", models.SmallIntegerField(default=1)),
                ("test_result", models.FloatField(blank=True, default=0.0)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applies",
                        to="job.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "applications",
                "ordering": ["id"],
                "unique_together": {("user", "job")},
            },
        ),
    ]
