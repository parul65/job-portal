# Generated by Django 5.2.1 on 2025-05-24 15:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0002_remove_job_job_type_remove_job_salary_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="application",
            name="cover_letter",
        ),
        migrations.RemoveField(
            model_name="application",
            name="resume",
        ),
        migrations.RemoveField(
            model_name="company",
            name="description",
        ),
        migrations.AlterField(
            model_name="application",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="jobs.job",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="posted_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
