# Generated by Django 4.0.2 on 2022-02-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='egn',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
