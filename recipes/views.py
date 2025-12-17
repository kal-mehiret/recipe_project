from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Recipe
from .forms import RecipeForm

def recipe_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'All')
    
    recipes = Recipe.objects.all().order_by('-date_created')
    
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) | Q(ingredients__icontains=query)
        )
        
    if category and category != 'All':
        recipes = recipes.filter(category=category)

    # Render the main list template which includes the search bar and filters
    # This ensures the UI remains consistent even when searching
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'query': query,
        'selected_category': category
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Add Recipe'})

@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author:
        return redirect('recipe_detail', pk=pk)
        
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Edit Recipe'})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user == recipe.author:
        if request.method == 'POST':
            recipe.delete()
            return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})