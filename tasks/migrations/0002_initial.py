# Generated by Django 5.0.6 on 2024-06-02 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tasks", "0001_initial"),
        ("tasks_category", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="task_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks_category.taskcategory",
            ),
        ),
    ]
