# Generated by Django 3.2.6 on 2021-12-08 16:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_alter_post_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 16, 21, 20, 331100, tzinfo=utc)),
        ),
    ]