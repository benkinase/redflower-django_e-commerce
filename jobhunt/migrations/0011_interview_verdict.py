# Generated by Django 3.1.7 on 2021-06-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunt', '0010_auto_20210529_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='verdict',
            field=models.CharField(choices=[('bad', 'bad'), ('ok', 'ok'), ('good', 'good'), ('v.good', 'v.good')], default='good', max_length=32),
        ),
    ]
