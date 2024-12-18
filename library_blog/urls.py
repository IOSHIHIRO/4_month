from django.urls import path

from . import views

urlpatterns = [
    path('', views.LibraryList.as_view(), name='library_list'),
    path('library_detail/<int:id>/', views.LibraryDetailsView.as_view(), name='library_detail'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_pets/', views.about_pets, name='about_pets'),
    path('system_time/', views.system_time, name='system_time'),
    path('comment/', views.CommentListView.as_view(), name='library_comment'),
    path('comment_view/', views.CommentView.as_view(), name='comment_view'),
    path('search/', views.SearchView.as_view(), name='search'),
]