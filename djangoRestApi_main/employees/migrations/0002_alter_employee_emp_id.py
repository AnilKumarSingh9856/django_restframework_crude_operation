# Generated by Django 5.1.7 on 2025-03-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="emp_id",
            field=models.IntegerField(max_length=10),
        ),
    ]
