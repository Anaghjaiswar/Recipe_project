from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe,ContactMessage
from .forms import RecipeForm

def home(request):
    return render(request, 'recipes/home.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

from django.shortcuts import render, redirect
from .forms import RecipeForm  # Assuming you have a form for the recipe

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()  # Save the new recipe
            return redirect('recipe_list')  # Redirect to the recipe list after saving
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


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