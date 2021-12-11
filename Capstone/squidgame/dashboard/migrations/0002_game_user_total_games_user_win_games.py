# Generated by Django 4.0 on 2021-12-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('single_player', models.BooleanField(default=True)),
                ('multiplayer', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='total_games',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='win_games',
            field=models.IntegerField(default=0),
        ),
    ]
