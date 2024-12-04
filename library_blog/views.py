from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Первый дз')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('🦁 🐅 🐯 ')

def  system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))