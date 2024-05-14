from django.test import TestCase
from .forms import RecipeSearchForm

class RecipeSearchFormTest(TestCase): 
  def test_valid_form(self):
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