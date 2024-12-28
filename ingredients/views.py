from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy
from .forms import CollectionForm
from django.views import generic



class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')


class CollectionCreateView(CreateView):
    model = CollectionForm
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_url = reverse_lazy('collection_list')


class CollectionListView(ListView):
    model = CollectionForm
    template_name = 'collections/collection_list.html'
    context_object_name = 'collections'


class DeleteRecipeView(generic.DeleteView):
    template_name = 'recipes/recipe_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(Recipe, id=basket_id)