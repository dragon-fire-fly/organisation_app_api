# Generated by Django 3.2.4 on 2023-05-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='../sd2as2klixs1ijw9022d', upload_to='images/'),
        ),
    ]
