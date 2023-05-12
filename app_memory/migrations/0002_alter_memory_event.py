# Generated by Django 3.2.4 on 2023-05-12 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0002_alter_event_image'),
        ('app_memory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memories', to='app_event.event'),
        ),
    ]
