# Generated by Django 3.1.3 on 2020-12-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_settings_alarm_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='location',
            field=models.CharField(default='cosna', max_length=20),
        ),
    ]
