# Generated by Django 3.2.4 on 2023-05-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0005_event_calendars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255),
        ),
    ]
