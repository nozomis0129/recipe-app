from django.urls import path
from .views import (
    welcome,
    RecipeListView,
    RecipeDetailView,
    search_recipes,
    about,
    add_recipe,
)

app_name = "recipes"

urlpatterns = [
    path("", welcome, name="home"),
    path("list/", RecipeListView.as_view(), name="list"),
    path("list/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("search/", search_recipes, name="search"),
    path("about/", about, name="about"),
    path("add_recipe/", add_recipe, name="add_recipe"),
]
