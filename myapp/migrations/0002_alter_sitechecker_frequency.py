# Generated by Django 5.0.8 on 2024-08-29 02:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitechecker',
            name='frequency',
            field=models.DurationField(default=datetime.timedelta(seconds=60), help_text='Set the time interval for the task', null=True),
        ),
    ]
