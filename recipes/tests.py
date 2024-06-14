from django.test import TestCase
from .models import Recipe

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            cooking_time=5,
            ingredients="tea leaves, water, sugar",
            description="Add tea leaves to boiling water, then add sugar",
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_recipe_name_length(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(name_max_length, 120)

    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("ingredients").max_length
        self.assertEqual(max_length, 350)

    def test_difficuty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), "Easy")

    def get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), "/list/1")
