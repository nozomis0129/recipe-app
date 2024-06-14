from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text="in minutes")
    ingredients = models.CharField(max_length=350)
    description = models.TextField(max_length=500)
    pic = models.ImageField(upload_to="recipes/", default="no_imag.png")

    # Calculate difficulty
    def calculate_difficulty(self):
        separated_ingredients = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(separated_ingredients) < 4:
            difficulty = "Easy"
        elif self.cooking_time < 10 and len(separated_ingredients) >= 4:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and len(separated_ingredients) < 4:
            difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(separated_ingredients) >= 4:
            difficulty = "Hard"
        return difficulty

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})
