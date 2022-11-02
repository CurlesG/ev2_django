from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name = 'book_list' ),
    path('book/add', views.add_book, name = 'add_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('author', views.author_list, name = 'author_list' ),
    path('author/add', views.add_author, name = 'add_author'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('author/delete/<int:pk>/', views.author_delete, name='author_delete'),
    path('genre', views.genre_list, name = 'genre_list' ),
    path('genre/add', views.add_genre, name = 'add_genre'),
    path('genre/<int:pk>/', views.genre_detail, name='genre_detail'),
    path('genre/<int:pk>/edit/', views.genre_edit, name='genre_edit'),
    path('genre/delete/<int:pk>/', views.genre_delete, name='genre_delete'),
    path('publisher', views.publisher_list, name = 'publisher_list' ),
    path('publisher/add', views.add_publisher, name = 'add_publisher'),
    path('publisher/<int:pk>/', views.publisher_detail, name='publisher_detail'),
    path('publisher/<int:pk>/edit/', views.publisher_edit, name='publisher_edit'),
    path('publisher/delete/<int:pk>/', views.publisher_delete, name='publisher_delete'),
]