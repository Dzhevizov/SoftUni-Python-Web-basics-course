# Generated by Django 4.0.2 on 2022-04-18 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='image_URL',
            new_name='image',
        ),
    ]