from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.AllBooks.as_view(), name='all_books'),
    path('children/', views.ChildrenBooks.as_view(), name='children_books'),
    path('youth/', views.BooksForYouth.as_view(), name='books_for_youth'),
]