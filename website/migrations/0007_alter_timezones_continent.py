# Generated by Django 4.2.3 on 2023-08-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_location_timezones_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timezones',
            name='continent',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
