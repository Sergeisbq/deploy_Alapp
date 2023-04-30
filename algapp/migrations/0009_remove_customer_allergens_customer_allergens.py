# Generated by Django 4.2 on 2023-04-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0008_alter_menu_dish_id_alter_menu_restaurant_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='allergens',
        ),
        migrations.AddField(
            model_name='customer',
            name='allergens',
            field=models.ManyToManyField(to='algapp.allergens'),
        ),
    ]
