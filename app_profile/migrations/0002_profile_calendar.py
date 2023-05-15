# Generated by Django 3.2.4 on 2023-05-12 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_calendar", "0002_remove_calendar_events"),
        ("app_profile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="calendar",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_calendar.calendar",
            ),
            preserve_default=False,
        ),
    ]