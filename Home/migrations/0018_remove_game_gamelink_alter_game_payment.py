# Generated by Django 4.1.2 on 2022-10-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_rename_game_game_gamelink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gamelink',
        ),
        migrations.AlterField(
            model_name='game',
            name='payment',
            field=models.CharField(max_length=200),
        ),
    ]
