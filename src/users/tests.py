from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
  # setup a test user
  def setUpTestData():
    User.objects.create(name='Test User')

  def test_user_name(self):
    user = User.objects.get(id=1)
    field_label = user._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_user_name_max_length(self):
    user = User.objects.get(id=1)
    max_length = user._meta.get_field('name').max_length
    self.assertEqual(max_length, 100)

  def test_user_string(self):
    user = User.objects.get(id=1)
    string_repr = user.__str__()
    self.assertEqual(string_repr, 'Test User')