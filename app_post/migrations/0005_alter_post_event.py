# Generated by Django 3.2.4 on 2023-05-28 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_event", "0012_alter_event_event_type"),
        ("app_post", "0004_alter_post_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="app_event.event",
            ),
        ),
    ]
