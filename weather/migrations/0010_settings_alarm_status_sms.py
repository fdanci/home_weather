# Generated by Django 3.1.3 on 2020-12-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0009_auto_20201205_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='alarm_status_sms',
            field=models.CharField(default='off', max_length=4),
        ),
    ]