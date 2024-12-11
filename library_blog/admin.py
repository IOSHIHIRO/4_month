from django.contrib import admin
from library_blog.models import library_model, Review

admin.site.register(library_model)
admin.site.register(Review)
