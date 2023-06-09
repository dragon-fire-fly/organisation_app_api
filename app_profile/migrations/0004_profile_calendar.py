# Generated by Django 3.2.4 on 2023-05-12 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_calendar", "0002_remove_calendar_events"),
        ("app_profile", "0003_remove_profile_calendar"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="calendar",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_calendar.calendar",
            ),
        ),
    ]
