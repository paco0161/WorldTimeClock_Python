# Generated by Django 4.2.3 on 2023-08-30 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_timezones_alter_userclocks_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timezones',
            old_name='location',
            new_name='area',
        ),
    ]
