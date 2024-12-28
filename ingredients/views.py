from django.shortcuts import render, get_object_or_404
from ingredients.models import Recipe
from ingredients.forms import RecipeForm, IngredientForm
from django.views import generic


class CreateRecipeView(generic.CreateView):
    template_name = 'ingredient/create_recipe.html'
    form_class = IngredientForm
    success_url = '/ingredient_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateRecipeView, self).form_valid(form)

class IngredientListView(generic.ListView):
    template_name = 'ingredient/ingredient_list.html'
    context_object_name = 'ingredient_list'
    model = Recipe

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class IngredientDetailView(generic.DetailView):
    template_name = 'ingredient/ingredient_detail.html'
    context_object_name = 'ingredient_id'

    def get_object(self, **kwargs):
        ingredient_id = self.kwargs.get('id')
        return get_object_or_404(Recipe, id=ingredient_id)

class DeleteIngredientView(generic.DeleteView):
    template_name = 'ingredient/delete_ingredient.html'
    success_url = '/ingredient_list/'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Recipe, id=basket_id)



