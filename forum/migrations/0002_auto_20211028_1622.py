# Generated by Django 3.2.8 on 2021-10-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='date_created',
            new_name='time_created',
        ),
        migrations.AddField(
            model_name='forum',
            name='time_modifed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]