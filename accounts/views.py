from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from algapp.models import Customer, Restaurant, Menu
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# class ProfileView(DetailView):
#     model = UserProfile
#     template_name = 'profile.html'
#     context_object_name = 'profile'



@login_required
def customer_profile(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    context = {
        'user': user,
        'customer': customer,
    }
    return render(request, 'customer_profile.html', context)


@login_required
def restaurant_profile(request):
    rest_user = request.user
    rest_customer = Restaurant.objects.get(user=rest_user)
    menus = Menu.objects.filter(restaurant_id=rest_customer.id)
    dishes = []
    
    for menu in menus:
        dishes.extend(menu.dish_id.all())

    dishes = list(set(dishes))
    dishes.reverse()
    print(dishes)
    context = {
        'dishes': dishes,
        'rest_user': rest_user,
        'rest_customer': rest_customer,
    }
    return render(request, 'restaurant_profile.html', context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile_redirect_view(request):
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('home_path')
    else:
        return redirect('home_path')


def create_profile_view(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts-all')
        
    user = request.user
    user_id = request.user.id
    form = ProfileForm(initial={'user': user, 'user_id': user_id})
    context = {'form': form}
    return render(request, 'create_profile.html', context)
