# Generated by Django 4.2.1 on 2023-08-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
