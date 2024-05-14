from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
  # model definition
  name = models.CharField(max_length=100)
  ingredients = models.CharField(max_length=400, help_text="Separate ingredients with a comma")
  cooking_time = models.PositiveSmallIntegerField(help_text='in minutes')
  directions = models.TextField(default='no directions')
  difficulty = models.CharField(max_length=20, blank=True, help_text='Leave blank, this will be auto-calculated')
  image = models.ImageField(upload_to='recipes', default='no_image.svg')

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
  
  # gets url for each recipe list item based on primary key (id)
  def get_absolute_url(self):
    return reverse ('recipes:details', kwargs={'pk': self.pk})
  
  def save(self, *args, **kwargs):
    self.difficulty = self.calculate_difficulty()
    super().save(*args, **kwargs)
