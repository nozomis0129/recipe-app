from django.urls import path
from .views import recipes_home

app_name = "users"

urlpatterns = [path("", recipes_home)]
