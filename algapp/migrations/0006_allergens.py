# Generated by Django 4.2 on 2023-04-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0005_alter_restaurant_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
        ),
    ]
