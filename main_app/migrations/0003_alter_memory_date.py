# Generated by Django 3.2.9 on 2021-11-28 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_memory_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
