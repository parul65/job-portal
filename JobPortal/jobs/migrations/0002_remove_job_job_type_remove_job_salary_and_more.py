# Generated by Django 5.2.1 on 2025-05-24 15:37

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="job_type",
        ),
        migrations.RemoveField(
            model_name="job",
            name="salary",
        ),
        migrations.AddField(
            model_name="company",
            name="location",
            field=models.CharField(default="Delhi", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="company",
            name="website",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="job",
            name="posted_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Date Posted"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="job",
            name="location",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="job",
            name="title",
            field=models.CharField(max_length=255),
        ),
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
                ("cover_letter", models.TextField(blank=True, null=True)),
                ("resume", models.FileField(upload_to="resumes/")),
                ("applied_at", models.DateTimeField(auto_now_add=True)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.job"
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
        ),
    ]
