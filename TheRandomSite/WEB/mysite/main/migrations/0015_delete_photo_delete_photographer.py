# Generated by Django 4.1.3 on 2022-12-08 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_fan_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Photographer',
        ),
    ]
