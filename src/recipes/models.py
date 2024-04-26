from django.db import models

# Create your models here.
class Recipe(models.Model):
  # model definition
  name = models.CharField(max_length=100)
  ingredients = models.CharField(max_length=400)
  cooking_time = models.PositiveSmallIntegerField(help_text='in minutes')
  directions = models.TextField(default='no directions')
  image = models.ImageField(upload_to='images', default='no_image.svg')

  # calculates difficulty of the recipe
  def calculate_difficulty(self):
    ingredients = self.ingredients.split(', ')
    if self.cooking_time < 15 and len(ingredients) < 5:
      difficulty = 'Easy'
    if self.cooking_time < 15 and len(ingredients) >= 5:
      difficulty = 'Medium'
    if self.cooking_time >= 15 and len(ingredients) < 5:
      difficulty = 'Intermediate'
    if self.cooking_time >= 15 and len(ingredients) >= 5:
      difficulty = 'Hard'

    return difficulty
  
  # string representation of the recipe
  def __str__(self):
    return str(self.name)
