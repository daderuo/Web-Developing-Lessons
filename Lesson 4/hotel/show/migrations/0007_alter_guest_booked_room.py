# Generated by Django 3.2.6 on 2021-08-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0006_alter_guest_booked_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='booked_room',
            field=models.ManyToManyField(blank=True, related_name='b_room', to='show.Hotel'),
        ),
    ]
