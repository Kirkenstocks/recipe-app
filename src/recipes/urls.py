from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, add_recipe, update_recipe, delete_recipe

app_name = 'recipes'

urlpatterns = [
  path('', home),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='details'),
  path('add_recipe/', add_recipe, name='add_recipe'),
  path('update_recipe/<pk>', update_recipe, name='update_recipe'),
  path('delete_recipe/<pk>', delete_recipe, name='delete_recipe'),
]