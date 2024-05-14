from io import BytesIO
import base64
import matplotlib.pyplot as plt
from collections import Counter

# handles low-level image details
def get_graph():
  buffer = BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)
  image_png = buffer.getvalue()
  graph = base64.b64encode(image_png)
  graph = graph.decode('utf-8')
  buffer.close()

  return graph

# gathers data and displays bar chart with most used ingredients
def get_bar_chart(recipes):
  all_ingredients = []

  # separate ingredient strings and add ingredients to all_ingredients
  for recipe in recipes:
    ingredient_list = recipe['ingredients'].split(', ')
    for ingredient in ingredient_list:
      ingredient = ingredient.strip().lower()
      if len(ingredient) > 12:
        short_ingredient = ingredient[:11] + '...'
        all_ingredients.append(short_ingredient)
      else:
        all_ingredients.append(ingredient)

  # get count of how many recipes each ingredient is in and assign to 2 variables
  ingredient_count = Counter(all_ingredients)
  ingredients, counts = zip(*ingredient_count.most_common(10)) if all_ingredients else([], [])
  
  plt.switch_backend('AGG') #AGG used for PNG files
  plt.figure(figsize=(8,4)) #set figure size

  # define plot if ingredients and counts variables exist
  if ingredients and counts:
    plt.bar(ingredients, counts)
    plt.xlabel('Ingredients')
    plt.ylabel('Number of Recipes')
    plt.title('Most Used Ingredients')
    plt.xticks(rotation=30) 
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1)) #sets y-axis interval to 1

   
  else:
    plt.text(1, 1, 'No ingredient data')
  
  # specify layout details and render graph to file
  plt.tight_layout()
  chart = get_graph()
  plt.close() #close plt to free up memory
  return chart

# gathers data and displays pie chart with recipe difficulty distribution
def get_pie_chart(recipes):
  recipe_difficulties = []

  # add the difficulty of each recipe to the recipe_difficulties list
  [recipe_difficulties.append(recipe['difficulty']) for recipe in recipes]

  # get a count of each difficulty
  difficulty_count = Counter(recipe_difficulties)

  plt.switch_backend('AGG') #AGG used for PNG files
  plt.figure(figsize=(8,4)) #set figure size

  # define plot if recipe difficulties are found
  if difficulty_count:
    plt.pie(difficulty_count.values(), labels=difficulty_count.keys(), autopct='%1.1f%%')
    plt.title('Difficulty of Recipes')
  else: 
    plt.text(1, 1, 'No difficulty data')
  
  # specify layout details and render graph to file
  plt.tight_layout()
  chart = get_graph()
  plt.close() #close plt to free up memory
  return chart
  
# gathers data and displays line chart showing cooking time 1st 10 recipes
def get_line_chart(recipes):
  recipe_list = []
  cooking_time_list = []

  while len(recipe_list) <= 10:
    for recipe in recipes:
      if len(recipe['name']) > 12:
        short_name = recipe['name'][:11] + '...'
        recipe_list.append(short_name)
      else:
        recipe_list.append(recipe['name'])
      
      cooking_time_list.append(recipe['cooking_time'])

  # combine the lists, sort both by recipe name, then separate again to fix double line bug
  recipe_list, cooking_time_list = (list(i) for i in zip(*sorted(zip(recipe_list, cooking_time_list))))

  plt.switch_backend('AGG') #AGG used for PNG files
  plt.figure(figsize=(8,4)) #set figure size

  if recipe_list and cooking_time_list:
    plt.plot(recipe_list, cooking_time_list, marker='o', linestyle='--')
    plt.xlabel('Recipes')
    plt.ylabel('Cooking Time')
    plt.title('Cooking Time of Recipes')
    plt.xticks(rotation=45)
  else:
    plt.text(1, 1, 'No difficulty data')

  # specify layout details and render graph to file
  plt.tight_layout()
  chart = get_graph()
  plt.close() #close plt to free up memory
  return chart