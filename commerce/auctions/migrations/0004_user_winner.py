# Generated by Django 3.2.6 on 2021-09-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210904_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='winner',
            field=models.ManyToManyField(blank=True, related_name='winner', to='auctions.Listing'),
        ),
    ]
