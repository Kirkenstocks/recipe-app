from django import forms
from django.forms import TextInput, NumberInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe

# define chart selection choices
chart_choices = (
  ('bar chart', 'Bar chart of most used ingredients'),
  ('pie chart', 'Pie chart of recipe difficulty distribution'),
  ('line chart', 'Line chart of cooking time of each recipe')
)

# define the search form implemented in recipes_list.html
class RecipeSearchForm(forms.Form):
  recipe_name = forms.CharField(required=False, max_length=100)
  ingredient = forms.CharField(required=False, max_length=100)
  min_cooking_time = forms.IntegerField(required=False, min_value=0, label='Minimum cooking time:')
  max_cooking_time = forms.IntegerField(required=False, min_value=0, label='Maximum cooking time:')
  chart_type = forms.ChoiceField(choices=chart_choices, required=False, label='Chart selection')

# define a form for adding and updating recipes
class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    fields = ['name', 'ingredients', 'cooking_time', 'directions', 'difficulty', 'image']
    # adding customization to the form field widgets
    widgets = {
      'name': TextInput(attrs={'class': 'form-control'}),
      'ingredients': TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ingredient 1, ingredient 2, ingredient 3'
        }),
      'cooking_time': NumberInput(attrs={'class': 'form-control'}),
      'directions': Textarea(attrs={
        'class': 'form-control',
        'style': 'height: 10vh;'
      })
    }

# define a user registration form
class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']