# Generated by Django 4.1.2 on 2022-10-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0004_alter_company_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="image",
            field=models.ImageField(blank=True, default="", upload_to=""),
        ),
    ]
