# Generated by Django 4.2.3 on 2023-07-19 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 19, 36, 30, 541101)),
        ),
    ]
