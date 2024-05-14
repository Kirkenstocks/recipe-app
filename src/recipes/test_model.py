from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
  # setup a test recipe
  def setUpTestData():
    Recipe.objects.create(
      name='Tea', 
      ingredients='Tea Leaves, Water, Sugar', 
      cooking_time=5,
      directions='Boil water, pour water over tea, allow tea to steep for at least 5 minutes, remove tea, add sugar as desired'  
    )

  # model test cases
  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_recipe_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 100)

  def test_recipe_ingredients(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('ingredients').verbose_name
    self.assertEqual(field_label, 'ingredients')

  def test_recipe_ingredients_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length
    self.assertEqual(max_length, 400)

  def test_recipe_cooking_time(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('cooking_time').verbose_name
    self.assertEqual(field_label, 'cooking time')

  def test_recipe_cooking_time_help_text(self):
    recipe = Recipe.objects.get(id=1)
    help_text = recipe._meta.get_field('cooking_time').help_text
    self.assertEqual(help_text, 'in minutes')

  def test_recipe_directions(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('directions').verbose_name
    self.assertEqual(field_label, 'directions')

  def test_recipe_image(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('image').verbose_name
    self.assertEqual(field_label, 'image')

  def test_default_image(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.image, 'no_image.svg')

  # test the calculate_difficulty function
  def test_recipe_difficulty(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.calculate_difficulty(), 'Easy')

  def test_recipe_string(self):
    recipe = Recipe.objects.get(id=1)
    string_repr = recipe.__str__()
    self.assertEqual(string_repr, 'Tea')

  # test the get_absolute_url function to ensure correct recipe is picked
  def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.get_absolute_url(), '/list/1')

  # test the overriden save method
  def test_save_method(self):
    recipe = Recipe.objects.get(id=1)
    recipe.cooking_time = 25
    recipe.save()
    self.assertEqual(recipe.difficulty, 'Intermediate')