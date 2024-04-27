from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, RecipeCategory
from .forms import RecipeForm, RecipeCategoryForm, UserRegistrationForm


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    preparation_steps = recipe.preparation_steps.split('Шаг ')
    preparation_steps = [step for step in preparation_steps if step]  # Убираем пустые элементы
    return render(request, 'recipes_app/recipe_detail.html', {'recipe': recipe, 'preparation_steps': preparation_steps})


def recipe_list(request):
    recipes = Recipe.objects.all()  # Получаем первые 5 рецептов
    return render(request, 'recipes_app/recipe_list.html', {'recipes': recipes})


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id) # Перенаправление на страницу с деталями рецепта
    else:
        form = RecipeForm()
    return render(request, 'recipes_app/recipe_create.html', {'form': form})


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        raise Http404("Вы не можете редактировать этот рецепт.")

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes_app/recipe_edit.html', {'form': form})


def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list') # Перенаправление на страницу со списком рецептов
    return render(request, 'recipes_app/recipe_delete.html', {'recipe': recipe})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'recipes_app/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'recipes_app/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/') # Перенаправление на главную страницу после успешного входа
            else:
                return render(request, 'recipes_app/login.html', {'error_message': 'Ваш аккаунт был отключен'})
        else:
            return render(request, 'recipes_app/login.html', {'error_message': 'Неверный логин'})
    else:
        return render(request, 'recipes_app/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('recipe_list')
