# Generated by Django 3.2.6 on 2021-09-04 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_user_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='auction',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.listing'),
        ),
        migrations.AddField(
            model_name='comments',
            name='text',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
