from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
# defines the home page
def home(request):
  return render(request, 'recipes/recipes_home.html')

# defines the recipe list view
class RecipeListView(ListView):
  model = Recipe
  template_name = 'recipes/recipes_list.html'

# defines the recipe details view
# appears when user clicks on the recipe name from list view
class RecipeDetailView(DetailView):
  model = Recipe
  template_name = 'recipes/recipe_details.html'