# Generated by Django 4.1.3 on 2022-12-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_fanclub_fan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fan',
            name='email',
        ),
    ]
