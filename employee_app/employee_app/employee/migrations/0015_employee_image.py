# Generated by Django 4.0.2 on 2022-02-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_alter_employee_egn'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
