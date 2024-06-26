from django import forms

# specify choices as a tuple
CHART__CHOICES = (
    ("#1", "Bar chart"),
    ("#2", "Pie chart"),
)

DIFF__CHOICES = (
    ("#1", "Easy"),
    ("#2", "Medium"),
    ("#3", "Intermediate"),
    ("#4", "Hard"),
)


# define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFF__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
