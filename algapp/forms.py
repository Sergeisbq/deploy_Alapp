from django import forms 
from .models import Customer, Restaurant, Menu, Ingredients, DishesIng


class CustomerForm(forms.ModelForm):
    search_query = forms.CharField(required=False, label='Search Allergens')

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'user')
        widgets = {
            'user': forms.HiddenInput(),
        }

    allergens = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'allergen-checkbox scroll-div'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['allergens'].required = False

    def filter_allergens(self):
        queryset = self.cleaned_data['allergens']
        search_query = self.cleaned_data['search_query']

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset






# class CustomerForm(forms.ModelForm):

#     class Meta: 
#         model = Customer
#         fields = ('first_name', 'last_name', 'email', 'user')
#         widgets = {
#             'user': forms.HiddenInput(),
#         }
        
#     allergens = forms.ModelMultipleChoiceField(queryset=Ingredients.objects.all().order_by('name'), widget=forms.CheckboxSelectMultiple) 


class RestAddForm(forms.ModelForm):

    class Meta: 
        model = Restaurant
        fields = ('name', 'address')
        widgets = {
            'user': forms.HiddenInput(),
        }


class DishAddForm(forms.ModelForm):

    class Meta: 
        model = DishesIng
        fields = ('name',)
        # widgets = {
        #     'user': forms.HiddenInput(),
        # }
    dish_main_ingredients = forms.ModelMultipleChoiceField(queryset=Ingredients.objects.all().order_by('name')) 
    dish_var_ingredients = forms.ModelMultipleChoiceField(queryset=Ingredients.objects.all().order_by('name'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dish_var_ingredients'].required = False

class RestForm(forms.Form):

    rests = forms.ModelChoiceField(queryset=Restaurant.objects.all())


class IngAddForm(forms.ModelForm):

    class Meta: 
        model = Ingredients
        fields = ('name',)









    