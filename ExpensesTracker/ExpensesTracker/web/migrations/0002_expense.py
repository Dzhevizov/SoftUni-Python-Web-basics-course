# Generated by Django 4.0.4 on 2022-04-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
