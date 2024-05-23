from django import forms

# define chart selection choices
chart_choices = (
  ('bar chart', 'Bar chart of most used ingredients'),
  ('pie chart', 'Pie chart of recipe difficulty distribution'),
  ('line chart', 'Line chart of cooking time of each recipe')
)

class RecipeSearchForm(forms.Form):
  recipe_name = forms.CharField(required=False, max_length=100)
  ingredient = forms.CharField(required=False, max_length=100)
  min_cooking_time = forms.IntegerField(required=False, min_value=0, label='Minimum cooking time:')
  max_cooking_time = forms.IntegerField(required=False, min_value=0, label='Maximum cooking time:')
  chart_type = forms.ChoiceField(choices=chart_choices, required=False, label='Chart selection')