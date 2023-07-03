import os
import django
from faker import Faker
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alg.settings')
django.setup()

from algapp.models import *

fake = Faker()


# Adding customers to db

list_of_allergens = ['celery', 'egg', 'fish', 'garlic', 'milk', 'mustard', 
                     'peanut', 'rice', 'sesame', 'soy', 'wallnut', 'honey', 
                     'almond', 'apple', 'orange', 'avocado', 'pepper', 'gluten',  
]

# if __name__ == '__main__':

#     print("Populating database, table 'Customer'")
#     for _ in range(5):
#         name = fake.name().split()
#         customer_algs = random.sample(list_of_allergens, 4)
#         new_customer = Customer(first_name = name[0],
#                                 last_name = name[1],
#                                 email = fake.unique.ascii_email(),
#                                 allergens = customer_algs
#                                 )
        # print(new_customer)
        # new_customer.save()


# algs = Customer.objects.all().values_list('allergens', flat=True)


### getting customers allergens from Customer table
# algs = Customer.objects.all().filter(id='1').values('allergens')
# algs_2 = list(algs[0].values())
# print(algs_2[0])

### getting dish ingridients from Dishes table
# dish = Dishes.objects.all().filter(id='4').values('dish')
# dish_2 = list(dish[0].values())
# print(dish_2[0])


### compairing customers allergens to dishes ingridients

# list_of_ingr = dish_2[0]
# print(sorted(list_of_ingr))
# allergen = algs_2[0]
# print(sorted(allergen))

# for j in range(len(allergen)):
    # if allergen[j] in list_of_ingr:
    #     print("No")
    #     print(allergen[j])
    #     break
    # else:
    #     pass



### Adding dishes to db

list_of_main_ingridients = ['celery', 'egg', 'fish', 'garlic', 'milk', 'mustard', 
                            'peanut', 'rice', 'soy', 'almond', 'apple', 'orange', 
                            'avocado', 'pear', 'shrimp', 'lamb', 'beef', 'coconut', 
                            'mushrooms', 'bacon','mayonnaise', 'corn', 'onion', 'turkey', 
                            'cheese', 'pork', 'salt', 'chicken', 'tomato', 'potato', 
                            'spinach', 'radish', 'leek', 'pumpkin', 'beans', 'zucchini',
                            'cucumber', 'kiwi', 'mango', 'blueberry', 'olives', 'lemon'
]

list_of_var_ingridients = ['sesame', 'wallnut', 'honey', 'pepper', 'chilie', 'sugar']

# if __name__ == '__main__':

#     print("Populating database, table 'Dishes'")
#     for _ in range(30):
#         name_1 = fake.language_name().split()
#         dish_main_ings_add = random.sample(list_of_main_ingridients, 8)
#         dish_var_ings_add = random.sample(list_of_var_ingridients, 2)
#         new_dish = Dishes(name = name_1[0],
#                         dish_main_ings = dish_main_ings_add,
#                         dish_var_ings = dish_var_ings_add
#                         )
#         print(new_dish)
#         new_dish.save()


### Adding restaurants to db

# dishes_for_restaurant = Dishes.objects.all()
# dishes_to_add = random.sample(dishes_for_restaurant, 10)
# print(dishes_for_restaurant)



# if __name__ == '__main__':

#     print("Populating database, table 'Restaurant'")
#     for _ in range(10):
#         name_1 = fake.language_name()
        
#         new_restaurant = Restaurant(name = name_1,
#                                 address = fake.address(),
#                                 )
#         print(new_restaurant)
#         new_restaurant.save()


# list_of_rests = Restaurant.objects.all().values_list('id', flat=True)
# print(type(list(list_of_rests)))
# list_of_dishes = Dishes.objects.all().all().values_list('id', flat=True)
# print(list_of_dishes)

# if __name__ == '__main__':

#     print("Populating database, table 'Menu'")
#     for _ in range(70):
#         restaurant_id_to_add = random.choice(list_of_rests)
        # dish_id_to_add = random.choice(list_of_dishes)
#         # Menu.restaurant_id.add(*restaurant_id_to_add)
#         # Menu.objects.create(restaurant_id = restaurant_id_to_add, dish_id = dish_id_to_add)
        
#         new_menu = Menu()
#         new_menu.save()
#         new_menu.restaurant_id.add(restaurant_id_to_add)
#         new_menu.dish_id.add(dish_id_to_add)

#         print(new_menu)
        # new_menu.save()


### Adding allergens to db
# if __name__ == '__main__':

#     print("Populating database, table 'Allergens'")
#     for i in range(len(list_of_allergens)):
#         name_1 = list_of_allergens[i]

#         new_allergen = Allergens(name = name_1,
#                         )
#         print(new_allergen)
#         new_allergen.save()


#  restautant: Restaurant,
def is_allergic(customer_id: int, dish_id: int) -> bool:

    person_algens = Customer.objects.all().get(id=customer_id)
    allergens = person_algens.allergens.all()
    dish = Dishes.objects.get(id=dish_id)
    
    ingredients = dish.dish
    print(allergens)
    print(dish)
    for allergen in allergens:
        if allergen.name in ingredients:
            print(f"FOUND ALLERGEN - {allergen}")
            return True
    return False

        

# is_allergic(12, 8)
# choose_dish = Menu.objects.all().filter(restaurant_id=8)
# print(choose_dish)
# for i in range(len(person_algens)):
#     a = list(person_algens[i].values())[0]
#     b = list(Allergens.objects.all().filter(id=a).values('id')[0].values())
#     if a == b[0]:
#         c = Allergens.objects.all().filter(id=a)[0]
#         print(c)
        # for i in c:
        #     print(i)
    

# a = list(person_algens[0].values())[0]
# b = list(Allergens.objects.all().filter(id=a).values('id')[0].values())
# print(a, b)
# if a == b[0]:
#     print(Allergens.objects.all().filter(id=a)[0])
    
# print(len(person_algens))
# b = list(Allergens.objects.all().filter(id=a).values('id')[0].values())
# print(b[0])

    
    
main_ingredients = ["Salt", "Pepper", "Olive oil", "Garlic", "Onion", "Tomato",
                    "Chicken", "Beef", "Rice", "Pasta", "Lemon", "Butter",
                    "Sugar", "Flour", "Eggs", "Milk", "Cheese", "Carrots", 
                    "Potatoes", "Cucumber", "Spinach", "Basil", "Parsley", 
                    "Thyme", "Oregano", "Cumin", "Paprika", "Ginger", "Soy sauce", 
                    "Vinegar", "Honey", "Mustard", "Chili powder", "Turmeric", "Bay leaves", 
                    "Nutmeg", "Cinnamon", "Coriander", "Celery", "Bell peppers", "Coconut milk", 
                    "Worcestershire sauce", "Sesame oil", "Balsamic vinegar", "Dill", "Rosemary", "Mint", 
                    "Red wine", "White wine", "Fish sauce", "Cilantro", "Lime", "Yogurt", 
                    "Hoisin sauce", "Green onions", "Black beans", "Cornstarch", "Mayonnaise", "Maple syrup", 
                    "Brown sugar", "Cayenne pepper", "Tofu", "Shrimp", "Salmon", "Crushed red pepper", 
                    "Anchovies", "Sour cream", "Parmesan cheese", "Cheddar cheese", "Blue cheese", "Ground turkey", 
                    "Ground cumin", "Ground coriander", "Ground ginger", "Tuna", "Coconut oil", "Sesame seeds", 
                    "Rose water", "Cardamom", "Ground cloves", "Almonds", "Cashews", "Peppermint extract", 
                    "Raisins", "Oats", "Quinoa", "Avocado", "Pineapple", "Orange", 
                    "Lime juice", "Zucchini", "Kale", "Red onion", "Brown rice", "Ground beef", 
                    "Ground pork", "Cocoa powder", "Tomato paste", "Tomato sauce", "Red pepper flakes", "Breadcrumbs", 
                    "Baking powder", "Baking soda", "Vanilla extract", "Ground cinnamon", "Chicken broth", "Peanut butter", 
                    "Apple", "Green beans", "Shallots", "Mushrooms", "Brussels sprouts", "Lentils", 
                    "Walnuts", "Sunflower seeds", "Poppy seeds", "Chia seeds", "Ground nutmeg", "Ground turmeric", 
                    "Ground paprika", "Ground cayenne pepper", "Barbecue sauce", "Salsa", "Sweet potatoes", "Provolone cheese",
                    "Ricotta cheese", "Artichokes", "Yellow onion", "Rosemary leaves", "Ground thyme", "Sage", 
                    "Parsnip", "Watermelon", "Red curry paste", "Pesto", "White vinegar", "Tabasco sauce", 
                    "Ground allspice", "Ground fennel", "Hazelnuts", "Pecans", "Flaxseed", "Seaweed", 
                    "Garam masala", "Crushed tomatoes", "Fresh ginger", "Cilantro leaves", "Tomato juice", "Pomegranate molasses", 
                    "Chickpeas", "Red lentils", "Wheat flour", "Chickpea flour", "Pita bread", "Popcorn", 
                    "Lavender", "Arrowroot powder", "Marjoram", "Bouillon cubes"]

print(len(main_ingredients))


if __name__ == '__main__':

    print("Populating database, table 'Ingredients'")
    for i in range(len(main_ingredients)):
        print(main_ingredients[i])

        new_ing = Ingredients(name = main_ingredients[i])
        print(new_ing)
        new_ing.save()

    