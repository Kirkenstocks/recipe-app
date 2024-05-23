from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from .models import Recipe
from .forms import RecipeSearchForm
from .utils import get_bar_chart, get_pie_chart, get_line_chart

# Create your views here.
# defines the home page
def home(request):
  return render(request, 'recipes/recipes_home.html')

# defines the recipe list view
class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/recipes_list.html'
  search_form = RecipeSearchForm()

  # customizes get_queryset method to retrieve recipe list based on search parameters
  def get_queryset(self):
    queryset = super().get_queryset()

    # extract parameters from the request object
    recipe_name = self.request.GET.get('recipe_name')
    ingredient = self.request.GET.get('ingredient')
    min_cooking_time = self.request.GET.get('min_cooking_time')
    max_cooking_time = self.request.GET.get('max_cooking_time')

    # filter the queryset based on provided parameters
    if recipe_name:
      queryset = queryset.filter(name__icontains=recipe_name)
    if ingredient:
      queryset = queryset.filter(ingredients__icontains=ingredient)
    #filter for cooking time input options
    if min_cooking_time and max_cooking_time:
      queryset = queryset.filter(cooking_time__gte=min_cooking_time, cooking_time__lte=max_cooking_time)
    elif min_cooking_time:
      queryset = queryset.filter(cooking_time__gte=min_cooking_time)
    elif max_cooking_time:
      queryset = queryset.filter(cooking_time__lte=max_cooking_time)

    # return the filtered queryset
    return queryset
  
  # customizes the get_context_data method and data added to context is passed to template
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)  #gather context data from parent class
    queryset = self.get_queryset()
    recipe_list = list(queryset.values('id', 'name', 'ingredients', 'cooking_time', 'directions', 'difficulty', 'image'))

    # pass search and chart select forms into context
    context['search_form'] = RecipeSearchForm(self.request.GET)

    # get the user selected chart and pass it to the template
    chart_selection = self.request.GET.get('chart_type')
    if chart_selection == 'bar chart': 
      context['bar_chart'] = get_bar_chart(recipe_list)
    elif chart_selection == 'pie chart':
      queryset = self.get_queryset()
      context['pie_chart'] = get_pie_chart(recipe_list)
    elif chart_selection == 'line chart':
      queryset = self.get_queryset()
      context['line_chart'] = get_line_chart(recipe_list)
    
    return context
  

# defines the recipe details view
# appears when user clicks on the recipe name from list view
class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/recipe_details.html'