# Generated by Django 3.2 on 2021-05-07 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_rename_skil_level_game_skill_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
