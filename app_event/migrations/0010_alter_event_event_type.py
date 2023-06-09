# Generated by Django 3.2.4 on 2023-05-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_event", "0009_alter_event_timezone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("Educational", "Educational"),
                    ("Cultural", "Cultural"),
                    ("Recreational", "Recreational"),
                    ("Fundraiser", "Fundraiser"),
                    ("Private", "Private"),
                    ("Work", "Work"),
                    ("Exhibition", "Exhibition"),
                    ("Festival", "Festival"),
                    ("Concert", "Concert"),
                    ("Cinema", "Cinema"),
                    ("Party", "Party"),
                    ("Seminar", "Seminar"),
                    ("Personal", "Personal"),
                    ("Other", "Other"),
                ],
                max_length=100,
            ),
        ),
    ]
