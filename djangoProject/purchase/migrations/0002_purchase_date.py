# Generated by Django 4.2.3 on 2023-07-19 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 19, 26, 50, 102380)),
        ),
    ]