# Generated by Django 3.2.6 on 2021-12-08 13:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_alter_post_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 13, 50, 4, 599913, tzinfo=utc)),
        ),
    ]
