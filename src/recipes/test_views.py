from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe

# tests for the Recipe views
class RecipeViewsTest(TestCase):
  def setUpTestData():
    User.objects.create_user(username='testuser', password='testpassword')
    Recipe.objects.create(
      name='Tea', 
      ingredients='Tea Leaves, Water, Sugar', 
      cooking_time=5,
      directions='Boil water, pour water over tea, allow tea to steep for at least 5 minutes, remove tea, add sugar as desired'  
    )

  # check that the home page loads correctly
  def test_home_view(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  # check that the recipe list view loads correctly
  def test_recipe_list_view(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)

  # check that the recipe detail view loads correctly
  def test_recipe_detail_view(self):
    self.client.login(username='testuser', password='testpassword')
    recipe = Recipe.objects.get(id=1)
    response = self.client.get(reverse('recipes:details', kwargs={'pk': recipe.pk}))
    self.assertEqual(response.status_code, 200)

  # check that if not logged in, user is redirected from list and detail views
  def test_list_view_login_required(self):
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 302)

  def test_detail_view_login_required(self):
    recipe = Recipe.objects.get(id=1)
    response = self.client.get(reverse('recipes:details', kwargs={'pk': recipe.pk}))
    self.assertEqual(response.status_code, 302)