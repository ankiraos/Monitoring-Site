# Generated by Django 5.0.8 on 2024-08-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_sitechecker_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitechecker',
            name='status',
            field=models.CharField(default='unknown', max_length=10),
        ),
    ]
