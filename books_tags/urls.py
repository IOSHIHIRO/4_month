from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('children/', views.children_books, name='children_books'),
    path('youth/', views.books_for_youth, name='books_for_youth'),
]