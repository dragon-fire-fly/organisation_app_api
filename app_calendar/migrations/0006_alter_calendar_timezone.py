# Generated by Django 3.2.4 on 2023-05-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_calendar', '0005_alter_calendar_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='timezone',
            field=models.CharField(default='Europe/Berlin', max_length=255),
        ),
    ]
