# Generated by Django 3.2.4 on 2023-06-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_event", "0012_alter_event_event_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="past",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
