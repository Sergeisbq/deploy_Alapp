# Generated by Django 4.2 on 2023-06-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0018_dishesing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_id',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='menus', to='algapp.dishesing'),
        ),
    ]
