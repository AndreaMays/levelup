# Generated by Django 3.2 on 2021-05-06 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_rename_user_game_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='skil_level',
            new_name='skill_level',
        ),
    ]
