from django.urls import path
from . import views

urlpatterns = [
    path('', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient_list/<int:id>/',views.IngredientDetailView.as_view(), name='Ingredient_detail'),
    path('ingredient_list/<int:id>/delete/', views.DeleteIngredientView.as_view(), name='Ingredient_delete'),
    path('create_recipe/', views.CreateRecipeView.as_view(), name='Ingredient_create'),
]