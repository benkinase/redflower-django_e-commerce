# Generated by Django 3.1.7 on 2021-06-06 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_auto_20210603_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 20, 58, 0, 232324)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 20, 58, 0, 232324)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 20, 58, 0, 232324)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 20, 58, 0, 232324)),
        ),
    ]
