from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<str:genre>/', views.book_list, name='book_list'),
    path('genres/<str:genre>/new_book/', views.book_create, name='book_create'),
    path('genres/<str:genre>/<str:book_url>/', views.book_detail, name='book_detail'),
]
