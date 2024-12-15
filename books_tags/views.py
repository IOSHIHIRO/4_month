from django.shortcuts import render, get_object_or_404
from . import models

def all_books(request):
    if request.method == 'GET':
        books = models.Book.objects.all().order_by('-id')
        context = {'books': books}
        return render(request, template_name='tags/all_books.html',context=context )

#Детские книги

def children_books(request):
    if request.method == 'GET':
        books_children = models.Book.objects.filter(tags__name='Книги для детей').order_by('-id')
        context = {'books_children': books_children}
        return render(request, template_name='tags/children_books.html',context=context)

def books_for_youth(request):
    if request.method == 'GET':
        books_for_yout = models.Book.objects.filter(tags__name='Книги для молодежи').order_by('-id')
        context = {'books_for_yout': books_for_yout}
        return render(request, template_name='tags/books_for_youth.html',context=context)

