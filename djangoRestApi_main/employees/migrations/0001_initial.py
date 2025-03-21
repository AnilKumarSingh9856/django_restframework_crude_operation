# Generated by Django 5.1.7 on 2025-03-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("emp_id", models.CharField(max_length=10)),
                ("emp_name", models.CharField(max_length=50)),
                ("designation", models.CharField(max_length=50)),
                ("company", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
            ],
        ),
    ]
