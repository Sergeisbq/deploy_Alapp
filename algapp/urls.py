"""
URL configuration for gifs_web project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import add_customer_view, rest, one_rest, add_rest_view, ask_chatGPT, update_profile_view, update_restaurant_view, add_dish_view, update_dish_view, add_ingredient, delete_dish_view, one_rest_no_red




urlpatterns = [
    path('', views.home, name="home_path"),
    path("add_customer/", add_customer_view, name='add_customer'),
    path("add_dish/", add_dish_view, name='add_dish'),
    path('delete_dish/<int:dish_id>/', delete_dish_view, name='delete_dish'),
    path("add_ingredient/", add_ingredient, name='add_ingredient'),
    path("update_dish/<int:d_id>", update_dish_view, name='update_dish'),
    path('update-customer/', update_profile_view, name='update_customer'), 
    path('update-restaurant/', update_restaurant_view, name='update_restaurant'), 
    path("restaurants/", rest, name='restaurants'), 
    path("add_restaurant/", add_rest_view, name='add_restaurant'), 
    path("restaurant/<int:r_id>", one_rest, name='restaurant'), 
    path("choose_dish/<int:r_id>", one_rest, name='dish_path'), 
    path("one_rest_no_red/<int:r_id>", one_rest_no_red, name='one_rest_no_red'),
    path('openai/ask/', ask_chatGPT, name='openai-ask'),
    path('openai/answer/', ask_chatGPT, name='answerOA'),

]