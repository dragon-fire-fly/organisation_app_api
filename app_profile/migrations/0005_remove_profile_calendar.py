# Generated by Django 3.2.4 on 2023-05-12 14:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_profile", "0004_profile_calendar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="calendar",
        ),
    ]