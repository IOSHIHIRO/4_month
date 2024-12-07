from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

def library_details_view(request, id):
    if request.method == 'GET':
        library_id = get_object_or_404(models.library_model, id=id)
        context = {
            'library_id': library_id,
        }
        return render(request, template_name='book_detail.html', context=context)


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