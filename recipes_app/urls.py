from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),  # Список рецептов
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Подробности рецепта
    path('recipe/create/', views.recipe_create, name='recipe_create'),  # Добавление рецепта
    path('recipe/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),  # Редактирование рецепта
    path('recipe/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),  # Удаление рецепта
    path('register/', views.register, name='register'),  # Регистрация нового пользователя
    path('accounts/login/', views.user_login, name='login'),  # Вход пользователя
    path('accounts/logout/', logout_view, name='logout'),   # Выход пользователя
]
