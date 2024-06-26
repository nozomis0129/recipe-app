from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart


# Create your views here.
def welcome(request):
    return render(request, "recipes/recipes_home.html")


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/details.html"


def search_recipes(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    recipe_diff = None
    qs = None
    chart = None

    # Check if the button is clicked
    if request.method == "POST":
        recipe_diff = request.POST.get("recipe_diff")
        chart_type = request.POST.get("chart_type")

        if recipe_diff == "#1":
            recipe_diff = "Easy"
        if recipe_diff == "#2":
            recipe_diff = "Medium"
        if recipe_diff == "#3":
            recipe_diff = "Intermediate"
        if recipe_diff == "#4":
            recipe_diff = "Hard"

        qs = Recipe.objects.all()

        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        # If data found
        if qs:
            # Convert the queryset values to panda's dataframe
            recipes_df = pd.DataFrame(qs.values("name", "cooking_time"))
            # display in terminal - needed for debugging during development only
            print(recipes_df)
            chart = get_chart(chart_type, recipes_df, labels=recipes_df["name"].values)

            recipes_df = pd.DataFrame(
                qs.values("id", "name", "cooking_time"),
                columns=["id", "name", "cooking_time"],
            )
            links = []
            for e, nam in enumerate(recipes_df["name"]):
                nam = (
                    '<a href="/list/'
                    + str(recipes_df["id"][e])
                    + '">'
                    + str(nam)
                    + "</a>"
                )
                links.append(nam)
            recipes_df["name"] = links
            # Convert the dataframe to HTML
            recipes_df = recipes_df.to_html(index=False, escape=False)

    context = {
        "form": form,
        "recipes_df": recipes_df,
        "recipe_diff": recipe_diff,
        "qs": qs,
        "chart": chart,
    }
    return render(request, "recipes/search.html", context)
