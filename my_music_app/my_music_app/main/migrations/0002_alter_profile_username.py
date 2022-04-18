# Generated by Django 4.0.2 on 2022-04-17 21:04

import django.core.validators
from django.db import migrations, models
import my_music_app.main.validator


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), my_music_app.main.validator.regex_validator]),
        ),
    ]
