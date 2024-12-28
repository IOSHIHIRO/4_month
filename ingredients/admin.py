from django.contrib import admin
from ingredients.models import Recipe, Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)

