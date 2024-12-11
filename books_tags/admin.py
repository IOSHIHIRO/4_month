from django.contrib import admin
from books_tags.models import Book, Tag

admin.site.register(Book)
admin.site.register(Tag)