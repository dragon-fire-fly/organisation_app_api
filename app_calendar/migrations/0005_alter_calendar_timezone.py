# Generated by Django 3.2.4 on 2023-05-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_calendar', '0004_auto_20230515_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='timezone',
            field=models.CharField(default='2023-05-15T09:43:51+02:00', max_length=255),
        ),
    ]