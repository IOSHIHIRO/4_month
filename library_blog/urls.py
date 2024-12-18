from django.urls import path

from . import views

urlpatterns = [
    path('', views.library_list, name='library_list'),
    path('library_detail/<int:id>/', views.library_details_view, name='library_detail'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_pets/', views.about_pets, name='about_pets'),
    path('system_time/', views.system_time, name='system_time'),
    path('comment/', views.comment_list_view, name='library_comment'),
    path('comment_view/', views.comment_view, name='comment_view'),
    path('search/', views.SearchView.as_view(), name='search'),
]