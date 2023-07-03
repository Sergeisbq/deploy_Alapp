from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm, RestForm, RestAddForm, DishAddForm, IngAddForm
from .models import Customer, Restaurant, Menu, Statistic, DishesIng
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
import random
from django.contrib.messages.views import SuccessMessageMixin
import json
import os
import openai
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()


def home (request):
    context={'title':'Home page'}
    return render(request, 'algapp/home.html', context)


def add_customer_view(request):
    if request.method == 'POST':
        customer_filled_form = CustomerForm(request.POST)
        if customer_filled_form.is_valid():
            new_customer = customer_filled_form.save()
            allergens = customer_filled_form.cleaned_data['allergens']
            new_customer.allergens.add(*allergens)
            context = {'new_customer': new_customer}
            return render(request, 'algapp/home.html', context)
        else:
            return HttpResponse(customer_filled_form.errors)

    if request.method == 'GET':
        customer_filled_form = CustomerForm(initial={"user": request.user})
        context = {'form': customer_filled_form}
        return render(request, 'algapp/add_customer.html', context)

    

def update_profile_view(request):
    customer = Customer.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        customer_filled_form = CustomerForm(request.POST, instance=customer)
        
        if customer_filled_form.is_valid():
            updated_customer = customer_filled_form.save()
            allergens = customer_filled_form.cleaned_data['allergens']
            updated_customer.allergens.set(allergens)
            
            context = {'updated_customer': updated_customer}
            return render(request, 'algapp/home.html', context)
        
        else:
            return HttpResponse(customer_filled_form.errors)

    if request.method == 'GET':
        allergens = customer.allergens.all()
        customer_filled_form = CustomerForm(instance=customer, initial={'allergens': allergens})
        context = {'form': customer_filled_form}
        return render(request, 'algapp/update_customer.html', context)
    

def add_rest_view(request):

    if request.method == 'POST':

        rest_filled_form = RestAddForm(request.POST) 

        if rest_filled_form.is_valid(): 
             restaurant = rest_filled_form.save(commit=False)
             restaurant.user = request.user
             restaurant.save()

            #  for _ in range(random.randint(12, 18)):

            #     list_of_dishes = Dishes.objects.all().all().values_list('id', flat=True)
            #     print(list_of_dishes)
            #     restaurant_id_to_add_1 = Restaurant.objects.latest('id')
            #     restaurant_id_to_add = restaurant_id_to_add_1.id
            #     dish_id_to_add = random.choice(list_of_dishes)
                
            #     new_menu = Menu()
            #     new_menu.save()
            #     new_menu.restaurant_id.add(restaurant_id_to_add)
            #     new_menu.dish_id.add(dish_id_to_add)

            #     print(new_menu)
            #     new_menu.save()
            
                # return HttpResponse("SUCCESSFULLY SAVED")
        
        else:
            pass

        return redirect('restaurant_profile')
        # return HttpResponseRedirect('/add_restaurant')
    

    if request.method == 'GET':
        print(request.user)
        rest_filled_form = RestAddForm() 
        context = {'form': rest_filled_form}
        return render(request, 'algapp/add_restaurant.html', context)


def update_restaurant_view(request):

    rest_customer = Restaurant.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        rest_filled_form = RestAddForm(request.POST, instance=rest_customer)
        
        if rest_filled_form.is_valid():
            updated_rest = rest_filled_form.save()
            
            context = {'updated_customer': updated_rest}
            return redirect('restaurant_profile')
            # return render(request, 'restaurant_profile', context)
        
        else:
            return HttpResponse(rest_filled_form.errors)

    if request.method == 'GET':
        rest_filled_form = RestAddForm(instance=rest_customer)
        context = {'form': rest_filled_form}
        return render(request, 'algapp/update_restaurant.html', context)


def is_allergic(request, dish_id: int): #customer_id: int, 
    person_algens = Customer.objects.get(user_id=request.user.id)
    allergens = person_algens.allergens.all()
    dish = DishesIng.objects.get(id=dish_id)
    
    ingredients_main = dish.dish_main_ingredients.all()
    ingredients_var = dish.dish_var_ingredients.all()
    
    found_allergens_main = []
    found_allergens_var = []
    
    for allergen in allergens:
        if allergen in ingredients_main:
            found_allergens_main.append(allergen)
        elif allergen in ingredients_var:
            found_allergens_var.append(allergen)

    return found_allergens_main, found_allergens_var


def all_rest(request):

    if request.method == 'POST':

        rest_form = RestForm(request.POST)

        if rest_form.is_valid():

            rest = rest_form.cleaned_data['rests']
            context = {'rest': rest}

            return render(request, 'algapp/restaurant.html', context)

    if request.method == 'GET':

        rest_form = RestForm()
        context = {'form': rest_form}

        return render(request, 'algapp/restaurants.html', context)
    

def rest (request):

    rests = Restaurant.objects.all()
    context={'rests': rests}
    return render(request, 'algapp/restaurants.html', context)
 


def one_rest(request, r_id):
    r = Restaurant.objects.get(pk=r_id)
    menus = Menu.objects.filter(restaurant_id=r.id)
    dishes = []

    for menu in menus:
        for dish in menu.dish_id.all():
            dishes.append(dish)

    if request.method == 'POST' and 'process_button' in request.POST:
        dishes_allergens = []
        for dish in dishes:
            found_allergens_main, found_allergens_var = is_allergic(request, dish.id)
            ingredients_main = dish.dish_main_ingredients.all()
            ingredients_var = dish.dish_var_ingredients.all()
            dishes_allergens.append((dish, found_allergens_main, found_allergens_var, ingredients_main, ingredients_var))
        
        context = {
            'dishes_allergens': dishes_allergens, 
            'r': r,
        }
        return render(request, 'algapp/choose_dish.html', context)
    
    context = {'r': r, 'dishes': dishes}
    return render(request, 'algapp/restaurant.html', context)


def one_rest_no_red(request, r_id):
    r = Restaurant.objects.get(pk=r_id)
    menus = Menu.objects.filter(restaurant_id=r.id)
    dishes = []

    for menu in menus:

        for dish in menu.dish_id.all():
            found_allergens_main, found_allergens_var = is_allergic(request, dish.id)
            if not found_allergens_main and not found_allergens_var:
                dishes.append(dish)
            elif found_allergens_var and not found_allergens_main:
                dishes.append(dish)


    if request.method == 'POST' and 'process_button' in request.POST:
        dishes_allergens = []
        for dish in dishes:
            found_allergens_main, found_allergens_var = is_allergic(request, dish.id)
            ingredients_main = dish.dish_main_ingredients.all()
            ingredients_var = dish.dish_var_ingredients.all()
            dishes_allergens.append((dish, found_allergens_var, ingredients_main, ingredients_var))
        
        context = {
            'dishes_allergens': dishes_allergens, 
            'r': r,
        }
        
        return render(request, 'algapp/one_rest_no_red.html', context)
    
    context = {'r': r, 'dishes': dishes}
    return render(request, 'algapp/restaurant.html', context)


@csrf_exempt
def ask_chatGPT(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    if request.method == 'POST':
        try:
            
            json_data = json.dumps(request.POST)
            data = json.loads(json_data)
            print(data['select_th'])
            api_key = os.getenv('OPENAI_API_KEY')
            openai.api_key = api_key
            promt1 = ''
            if data['select_th'] == 'Recipe':
                promt1 = 'Type a recipe for '
            elif data['select_th'] == 'Suggestion':
                promt1 = 'Reccomend me '
            else:
                promt1 = ''
            allergens = []
            for allergen in customer.allergens.all():
                allergens.append(allergen.name)
            promt2 = f" without {allergens}"
            print(promt2)
            print(promt1 + ' ' + data['prompt'] + promt2 + ' response as a JSON')

            
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=promt1 + ' ' + data['prompt'] + promt2 + ' response as a JSON',
                temperature=0,
                max_tokens=1500,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            print('This is a prompt ' + promt1 + data['prompt'] + ' response as a JSON')
            json_object = json.dumps(response, indent=4)

            with open("sample.json", "w") as outfile:
                outfile.write(json_object)

            with open('sample.json') as file:
                json_data = json.load(file)
                print(json_data)
                new_data = Statistic()
                new_data.file = json_data
                new_data.save()

                print(json_data['choices'][0]['text'])
                text = json_data['choices'][0]['text']
                print("----here text ----", text)
                context = {'response': json.loads(text)}

            return render(request, 'algapp/answerOA.html', context)

            # return JsonResponse(response, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        # return JsonResponse({'error': 'Invalid request method'}, status=405)
        return render(request, 'algapp/openai.html', {})



def add_dish_view(request):

    if request.method == 'POST':

        dish_filled_form = DishAddForm(request.POST)

        restaurant = Restaurant.objects.get(user_id=request.user.id)
        new_menu = Menu()
        new_menu.save()
        new_menu.restaurant_id.add(restaurant.id)

        if dish_filled_form.is_valid(): 
            new_dish = dish_filled_form.save() 
            dish_main_ingredients = dish_filled_form.cleaned_data['dish_main_ingredients']
            new_dish.dish_main_ingredients.add(*dish_main_ingredients) 
            dish_var_ingredients = dish_filled_form.cleaned_data['dish_var_ingredients']
            new_dish.dish_var_ingredients.add(*dish_var_ingredients) 
            dish_id_to_add = DishesIng.objects.latest('id')
            new_menu.dish_id.add(dish_id_to_add)
            new_menu.save()
            
            context = {'new_dish': new_dish}

            rest_customer = Restaurant.objects.get(user=request.user)
            context = {'rest_user': request.user,
                       'rest_customer': rest_customer,
                       'new_dish': new_dish,
                        }

            return redirect('restaurant_profile')
            # return render(request, 'restaurant_profile.html', context)
        
        else:

            return HttpResponse(dish_filled_form.errors)

    if request.method == 'GET':

        dish_filled_form = DishAddForm()
        context = {'form': dish_filled_form,
                   }
        return render(request, 'algapp/add_dish.html', context)
    


def update_dish_view(request, d_id):
    dish = DishesIng.objects.get(id=d_id)
    dish_main_ingredients = dish.dish_main_ingredients.all()
    dish_var_ingredients = dish.dish_var_ingredients.all()
    context = {'dish': dish}

    if request.method == 'POST':

        dish_filled_form = DishAddForm(request.POST, instance=dish)

        if dish_filled_form.is_valid(): 
            updated_dish = dish_filled_form.save() 
            dish_main_ingredients = dish_filled_form.cleaned_data['dish_main_ingredients']
            updated_dish.dish_main_ingredients.set(dish_main_ingredients) 
            dish_var_ingredients = dish_filled_form.cleaned_data['dish_var_ingredients']
            updated_dish.dish_var_ingredients.set(dish_var_ingredients) 
            
            return redirect('restaurant_profile')
        
        else:

            return HttpResponse(dish_filled_form.errors)

    if request.method == 'GET':

        dish_filled_form = DishAddForm(instance=dish, initial={'name': dish.name,
                                                'dish_main_ingredients': dish_main_ingredients,
                                                'dish_var_ingredients': dish_var_ingredients
                                                })
        context = {'form': dish_filled_form}
        return render(request, 'algapp/update_dish.html', context)
    
def delete_dish_view(request, dish_id):
    dish = get_object_or_404(DishesIng, id=dish_id)

    if request.method == 'POST':
        dish.delete()
        return redirect('restaurant_profile')

    context = {'dish': dish}
    return render(request, 'algapp/delete_dish.html', context)

def add_ingredient(request):
    if request.method == 'POST':
        form = IngAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_dish') 
    else:
        form = IngAddForm()
    
    context = {'form': form}
    return render(request, 'algapp/add_ingredient.html', context)


