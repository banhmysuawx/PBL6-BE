# Generated by Django 4.1.2 on 2022-11-24 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("comment_posts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DisLikeComment",
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
                (
                    "dislike_comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dislike_comments",
                        to="comment_posts.commentpost",
                    ),
                ),
                ("dislike_user", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "db_table": "like_comments",
            },
        ),
    ]
