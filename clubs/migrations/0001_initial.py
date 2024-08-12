# Generated by Django 5.1 on 2024-08-12 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Club",
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
                ("name", models.CharField(max_length=255)),
                ("teacher_id", models.IntegerField()),
                ("info", models.TextField()),
                ("ph", models.TextField()),
                ("able1", models.IntegerField()),
                ("able2", models.IntegerField()),
                ("able3", models.IntegerField()),
                ("now1", models.IntegerField()),
                ("now2", models.IntegerField()),
                ("now3", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ClubLog",
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
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        to="clubs.club",
                    ),
                ),
            ],
        ),
    ]
