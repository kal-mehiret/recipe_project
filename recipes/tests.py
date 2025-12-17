from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            ingredients='Ingredient 1',
            instructions='Step 1',
            category='Dinner',
            author=self.user
        )

    def test_recipe_content(self):
        self.assertEqual(f'{self.recipe.title}', 'Test Recipe')
        self.assertEqual(f'{self.recipe.category}', 'Dinner')
