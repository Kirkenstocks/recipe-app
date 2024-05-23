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
    response = self.client.get(reverse('recipes:details', args=[recipe.pk]))
    self.assertEqual(response.status_code, 200)

  # test recipe detail view if non-existent recipe is specified
  def test_nonexistent_recipe_detail_view(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('recipes:details', args=[404]))
    # recipe not found so 404 staus code returned
    self.assertEqual(response.status_code, 404)

  # check that if not logged in, user is redirected from list and detail views
  def test_list_view_login_required(self):
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 302)

  def test_detail_view_login_required(self):
    recipe = Recipe.objects.get(id=1)
    response = self.client.get(reverse('recipes:details', args=[recipe.pk]))
    self.assertEqual(response.status_code, 302)

  # test the add_recipe FBV
  def test_add_recipe_view(self):
    # login and setup data to be added as new recipe
    self.client.login(username='testuser', password='testpassword')
    data = {
      'name': 'Test recipe',
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': 10,
      'directions': 'do stuff'
    }
    url = reverse('recipes:add_recipe')

    # post request to add recipe and get new recipe
    response = self.client.post(url, data)
    recipe = Recipe.objects.get(id=2)

    # assert that a redirection happens on recipe addition and that a new recipe is added with all fields matching
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Recipe.objects.count(), 2)
    self.assertEqual(recipe.name, 'Test recipe')
    self.assertEqual(recipe.ingredients, 'ingredient1, ingredient2, ingredient3')
    self.assertEqual(recipe.cooking_time, 10)
    self.assertEqual(recipe.directions, 'do stuff')

  # test update recipe FBV
  def test_update_recipe_view(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
      'name': 'Tea changed',
      'ingredients': 'ingredient1, ingredient2, ingredient3',
      'cooking_time': 10,
      'directions': 'make tea'
    }
    # get recipe object and pass primary key to url
    recipe = Recipe.objects.get(id=1)
    url = reverse('recipes:update_recipe', args=[recipe.pk])

    # post request to update recipe and get updated recipe 
    response = self.client.post(url, data)
    recipe = Recipe.objects.get(id=1)

    # assert that a redirection happens on recipe update and that recipe is updated appropriately
    self.assertEqual(response.status_code, 302)
    self.assertEqual(recipe.name, 'Tea changed')
    self.assertEqual(recipe.ingredients, 'ingredient1, ingredient2, ingredient3')
    self.assertEqual(recipe.cooking_time, 10)
    self.assertEqual(recipe.directions, 'make tea')

  # test delete recipe FBV
  def test_delete_recipe_view(self):
    self.client.login(username='testuser', password='testpassword')

    # assert that there is 1 recipe in database
    self.assertEqual(Recipe.objects.count(), 1)

    # get recipe and pass pk to the url
    recipe = Recipe.objects.get(id=1)
    url = reverse('recipes:delete_recipe', args=[recipe.pk])

    # post request to delete desired recipe
    response = self.client.post(url)

    # assert that a redirection happens and that the recipe was deleted
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Recipe.objects.count(), 0)

  # test a successful user registration
  def test_user_registration(self):
    # setup data and url
    data = {
      'username': 'testuser2',
      'email': 'email@gmail.com',
      'password1': 'testpass123',
      'password2': 'testpass123'
    }
    url = reverse('register')

    # send POST request to create user
    response = self.client.post(url, data)

    # get the new user
    user = User.objects.get(id=2)

    # assert that a redirect happens and user is created with specified username and email
    self.assertEqual(response.status_code, 302)
    self.assertEqual(User.objects.count(), 2)
    self.assertEqual(user.username, 'testuser2')
    self.assertEqual(user.email, 'email@gmail.com')

  # test a user registration case where confirmation password is incorrect
  def test_user_registration_failure(self):
    data = {
      'username': 'testuser2',
      'email': 'email@gmail.com',
      'password1': 'testpass123',
      'password2': 'testpass12345'
    }
    url = reverse('register')
    # check that there is 1 user object (created during setUpTestData())
    self.assertEqual(User.objects.count(), 1)

    response = self.client.post(url, data)

    # form error causes re-render, giving 200 status code
    self.assertEqual(response.status_code, 200)
    # still only 1 user object
    self.assertEqual(User.objects.count(), 1)
    # check that expected form error is displayed
    self.assertContains(response, "The two password fields didn’t match.")