# Generated by Django 3.1.7 on 2021-05-29 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunt', '0006_auto_20210529_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='job_application',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='job_application',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='techstack',
            old_name='job_application',
            new_name='application',
        ),
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 9, 33, 28, 208215)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 9, 33, 28, 209214)),
        ),
    ]
