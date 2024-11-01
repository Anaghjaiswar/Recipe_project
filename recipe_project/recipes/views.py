from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe,ContactMessage
from .forms import RecipeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

def home(request):
    return render(request, 'recipes/home.html')

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            messages.success(request, "Logged in successfully!")
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'recipes/login.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if not User.objects.filter(username= email).exists():
                user = User.objects.create_user(
                    username=email,  # This is set to the email
                    email=email,  # Set the email field correctly
                    password=password
                )
                user.first_name = first_name
                user.last_name = last_name

                user.save()

                messages.success(request, "Your account has been created successfully!")
                return redirect("login")
            else:
                messages.error(request, "An account with this email already exists.")
        else:
            messages.error(request,"passwords do not match.")


    return render(request, 'recipes/signup.html')

@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

from django.shortcuts import render, redirect
from .forms import RecipeForm  

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save() 
            return redirect('recipe_list')  
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('recipe_list')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'recipes/change_password.html', {'form': form})

def recipe_update(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            if form.cleaned_data.get('delete_image') and recipe.recipe_image:
                recipe.recipe_image.delete()
                recipe.recipe_image = None
            form.save()
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

def about(request):
    return render(request, 'recipes/about.html') 


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('myname')
        email = request.POST.get('email')
        issue_type = request.POST.get('choices')
        message = request.POST.get('message')


        ContactMessage.objects.create(
            name=name,
            email=email,
            issue_type=issue_type,
            message=message
        )

        return HttpResponse("Thank you for your message! We will get back to you shortly.")

    return render(request, 'recipes/contact.html')