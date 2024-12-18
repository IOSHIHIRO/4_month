from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models
from library_blog.models import Review, library_model
from library_blog.forms import LibraryForm
from django.views import generic

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'library_li'
    paginate_by = 2

    def get_queryset(self):
        return models.library_model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class LibraryDetailsView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'library_id'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(library_model, id=basket_id)

# def library_details_view(request, id):
#     if request.method == 'GET':
#         library_id = get_object_or_404(models.library_model, id=id)
#         context = {
#             'library_id': library_id,
#         }
#         return render(request, template_name='book_detail.html', context=context)

class CommentView(generic.CreateView):
    template_name = 'comment.html'
    form_class = LibraryForm
    success_url = '/comment/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CommentView, self).form_valid(form)

# def comment_view(request):
#     if request.method == 'POST':
#         form = LibraryForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('library_comment')
#
#     else:
#         form = LibraryForm()
#     return render(request, template_name='comment.html', context={'form': form})

class CommentListView(generic.ListView):
    template_name = 'book_detail.html'
    context_object_name = 'comment_list'
    model = Review

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def comment_list_view(request):
#     if request.method == 'GET':
#         comment_list = Review.objects.all().order_by('-id')
#         context = {'comment_list': comment_list}
#         return render(request, template_name='book_detail.html', context=context)

class LibraryList(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'library_li'
    model = library_model

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def library_list(request):
#     if request.method == 'GET':
#         library_li = models.library_model.objects.all().order_by('-id')
#         context = {
#             'library_li': library_li
#         }
#         return render(request, template_name='book.html', context=context)

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Первый дз')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('🦁 🐅 🐯 ')

def  system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))