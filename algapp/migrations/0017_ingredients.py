# Generated by Django 4.2 on 2023-06-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algapp', '0016_alter_dishes_dish_var_ings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
        ),
    ]
