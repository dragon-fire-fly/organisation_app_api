# Generated by Django 3.2.4 on 2023-05-12 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_event", "0002_alter_event_image"),
        ("app_post", "0003_post_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_event.event",
            ),
        ),
    ]
