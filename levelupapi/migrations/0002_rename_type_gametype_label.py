# Generated by Django 3.2 on 2021-05-05 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gametype',
            old_name='type',
            new_name='label',
        ),
    ]
