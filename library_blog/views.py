from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models
from library_blog.models import Review
from library_blog.forms import LibraryForm



def library_details_view(request, id):
    if request.method == 'GET':
        library_id = get_object_or_404(models.library_model, id=id)
        context = {
            'library_id': library_id,
        }
        return render(request, template_name='book_detail.html', context=context)


def comment_view(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library_comment')

    else:
        form = LibraryForm()
    return render(request, template_name='comment.html', context={'form': form})

def comment_list_view(request):
    if request.method == 'GET':
        comment_list = Review.objects.all().order_by('-id')
        context = {'comment_list': comment_list}
        return render(request, template_name='book.html', context=context)


def library_list(request):
    if request.method == 'GET':
        library_li = models.library_model.objects.all().order_by('-id')
        context = {
            'library_li': library_li
        }
        return render(request, template_name='book.html', context=context)

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Первый дз')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('🦁 🐅 🐯 ')

def  system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))