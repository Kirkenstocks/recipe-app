from django.test import TestCase
from django.contrib.auth.models import User
from .forms import RecipeSearchForm, RecipeForm

class RecipeSearchFormTest(TestCase): 
  def test_valid_search_form(self):
    data = {
      'recipe_name': 'coffee',
      'ingredient': 'water',
      'min_cooking_time': 0,
      'max_cooking_time': 30
    }

    form = RecipeSearchForm(data=data)
    self.assertTrue(form.is_valid())

    # test if form is valid only partially filled (no fields are required)
    data = {
      'recipe_name': 'co',
      'min_cooking_time': 3
    }

    form = RecipeSearchForm(data=data)
    self.assertTrue(form.is_valid())

  def test_cooking_time_min_value(self):
    # check validation on the minimum cooking time field
    data = {
      'min_cooking_time': -3,
    }

    form = RecipeSearchForm(data=data)
    self.assertFalse(form.is_valid())

    # check validation on the maximum cooking time field
    data = {
      'max_cooking_time': -3
    }

    form = RecipeSearchForm(data=data)
    self.assertFalse(form.is_valid())

  def test_recipe_name_max_length(self):
    data = {'recipe_name': 'r' * 101}
    form = RecipeSearchForm(data=data)
    self.assertFalse(form.is_valid())

  def test_ingredient_max_length(self):
    data = {'ingredient': 'i' * 101}
    form = RecipeSearchForm(data=data)
    self.assertFalse(form.is_valid())

  # test that the form is valid when chart type is specified
  def test_chart_type(self):
    chart_types = ['bar chart', 'pie chart', 'line chart']

    for chart_type in chart_types:
      data = {'chart_type': chart_type}
      form = RecipeSearchForm(data=data)
      self.assertTrue(form.is_valid())

class RecipeFormTest(TestCase):
  # test that completely filled in form is valid
  def test_recipe_form_valid(self):
    data = {
      'name': 'Test name',
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': 10,
      'directions': 'do stuff',
      'image': 'image.jpg'
    }
    form = RecipeForm(data=data)
    self.assertTrue(form.is_valid())

  # test that partially filled in form (only required fields) is valid
  def test_partial_recipe_form_valid(self):
    data = {
      'name': 'Test name',
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': 10,
      'directions': 'no directions', #default text supplied by model
      'image': ''
    }
    form = RecipeForm(data=data)
    self.assertTrue(form.is_valid())

  # test that form without name is invalid as name is required
  def test_recipe_form_no_name(self):
    data = {
      'name': '',
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': 10,
      'directions': 'do stuff',
      'image': 'image.jpg'
    }
    form = RecipeForm(data=data)
    self.assertFalse(form.is_valid())

  # test that form with name that is over 100 char limit is invalid
  def test_recipe_form_long_name(self):
    data = {
      'name': 'n' * 101,
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': 10,
      'directions': 'do stuff',
      'image': 'image.jpg'
    }
    form = RecipeForm(data=data)
    self.assertFalse(form.is_valid())

  # test that form without ingredients is invalid as ingredients are required
  def test_recipe_form_no_ingredients(self):
    data = {
      'name': 'Test name',
      'ingredients': '',
      'cooking_time': 10,
      'directions': 'do stuff',
      'image': 'image.jpg'
    }
    form = RecipeForm(data=data)
    self.assertFalse(form.is_valid())

  # test that form with ingredients over 400 char limit is invalid
  def test_recipe_form_long_ingredients(self):
    data = {
      'name': 'Test name',
      'ingredients': 'i' * 401,
      'cooking_time': 10,
      'directions': 'do stuff',
      'image': 'image.jpg'
    }
    form = RecipeForm(data=data)
    self.assertFalse(form.is_valid())

  # test that form with no cooking time is invalid
  def test_recipe_form_no_cooking_time(self):
    data = {
      'name': 'Test name',
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': '',
      'directions': 'do stuff',
      'image': 'image.jpg'
    }
    form = RecipeForm(data=data)
    self.assertFalse(form.is_valid())

  # test that form with negative cooking time is invalid
  def test_recipe_form_invalid_cooking_time(self):
    data = {
      'name': 'Test name',
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': -3,
      'directions': 'do stuff',
      'image': 'image.jpg'
    }
    form = RecipeForm(data=data)
    self.assertFalse(form.is_valid())