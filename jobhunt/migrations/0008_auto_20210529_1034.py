# Generated by Django 3.1.7 on 2021-05-29 08:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunt', '0007_auto_20210529_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 10, 34, 50, 266979)),
        ),
        migrations.AlterField(
            model_name='interview',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='jobhunt.application'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 10, 34, 50, 268000)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='jobhunt.application'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 10, 34, 50, 268999)),
        ),
        migrations.AlterField(
            model_name='techstack',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='techstachs', to='jobhunt.application'),
        ),
    ]
