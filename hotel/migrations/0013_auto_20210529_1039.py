# Generated by Django 3.1.7 on 2021-05-29 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20210529_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 10, 39, 22, 642646)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 10, 39, 22, 642646)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 10, 39, 22, 644645)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 10, 39, 22, 644645)),
        ),
    ]
