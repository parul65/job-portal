# Generated by Django 5.2.1 on 2025-06-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0008_alter_job_salary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="salary",
            field=models.IntegerField(),
        ),
    ]
