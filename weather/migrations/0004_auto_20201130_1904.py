# Generated by Django 3.1.3 on 2020-11-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20201123_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='date',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
