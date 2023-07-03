from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Customer(models.Model):

    first_name = models.CharField(max_length=50, blank=False, db_index=True)
    last_name = models.CharField(max_length=50, blank=False, db_index=True)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    allergens = models.ManyToManyField('Ingredients')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class DishesIng(models.Model):
    
    name = models.CharField(max_length=50, blank=False, db_index=True)
    dish_main_ingredients = models.ManyToManyField('Ingredients', related_name='main_dishes')
    dish_var_ingredients = models.ManyToManyField('Ingredients', related_name='var_dishes')

    def __str__(self):
        return f"{self.name} {self.dish_main_ingredients.all()}"
    def list_ing(self):
        return ", ".join(self.dish_main_ingredients.all(), self.dish_var_ingredients.all())


class Restaurant(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)
    address = models.CharField(max_length=100, blank=False, db_index=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.address}"
    

class Menu(models.Model):

    restaurant_id = models.ManyToManyField('Restaurant', blank=True, db_index=True, related_name='menus')
    dish_id = models.ManyToManyField('DishesIng', blank=True, db_index=True, related_name='menus')

    def __str__(self):
        return f"{self.restaurant_id} {self.dish_id}"

    
class Ingredients(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name}"
    

class Statistic(models.Model):

    file = models.JSONField()



