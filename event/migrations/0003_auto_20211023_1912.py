# Generated by Django 3.2.7 on 2021-10-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_card_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Date',
            new_name='Tanggal',
        ),
        migrations.AddField(
            model_name='event',
            name='Sinopsis',
            field=models.TextField(default=''),
        ),
    ]