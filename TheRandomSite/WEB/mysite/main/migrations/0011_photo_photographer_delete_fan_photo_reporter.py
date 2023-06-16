# Generated by Django 4.1.3 on 2022-12-07 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_fan_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Fan',
        ),
        migrations.AddField(
            model_name='photo',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.photographer'),
        ),
    ]
