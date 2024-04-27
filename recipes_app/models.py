from django.contrib.auth.models import User
from django.db import models


class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Время приготовления в минутах")
    image = models.ImageField(upload_to='recipe_images/')
    ingredients = models.TextField(help_text="Перечислите ингредиенты и их количество")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.SET_NULL, null=True, blank=True)


class RecipeCategoryLink(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
