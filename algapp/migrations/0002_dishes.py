# Generated by Django 4.2 on 2023-04-29 10:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('dish', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
            ],
        ),
    ]
