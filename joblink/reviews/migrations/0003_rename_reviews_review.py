# Generated by Django 4.1.2 on 2022-10-28 10:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0006_alter_company_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reviews", "0002_alter_reviews_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reviews",
            new_name="Review",
        ),
    ]
