from django.shortcuts import render

# Create your views here.


def recipes_home(request):
    return render(request, "users/recipes_home.html")
