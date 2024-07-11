from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Define a function view called login_view that takes a request from user
def login_view(request):
    # Initialize
    error_message = None
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        # Check if form is valid
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            # If user is authenticated
            if user is not None:
                login(request, user)
                return redirect("recipes:list")
        else:
            error_message = "ooops, something went worng"

    context = {"form": form, "error_message": error_message}
    return render(request, "auth/login.html", context)


# Define a function view called logout_view that takes a request from user
def logout_view(request):
    logout(request)
    return render(request, "auth/success.html")
