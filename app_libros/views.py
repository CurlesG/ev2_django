from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render (request, 'book_detail.html', {'book':book})

def add_book(request):
  if request.method == "POST":
    form = BookForm(request.POST)
    if form.is_valid():
      book = form.save(commit=False)
      book.save()      
      # return redirect('car_detail', pk=car.pk)
      return redirect('book_list')
  else:
    form = BookForm()
  return render(request, 'book_edit.html', {'form': form})

def book_delete(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if request.method=='POST':
    book.delete()
    return redirect('book_list')
  return render(request, 'book_detail.html', {'book': book})

def book_edit(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if request.method == "POST":
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
      book = form.save(commit=False)
      book.save()
      return redirect('book_detail', pk=book.pk)
  else:
    form = BookForm(instance=book)
  return render(request, 'book_edit.html', {'form': form})

# Author

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'author_list': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render (request, 'author_detail.html', {'author':author})

def add_author(request):
  if request.method == "POST":
    form = AuthorForm(request.POST)
    if form.is_valid():
      author = form.save(commit=False)
      author.save()      
      return redirect('author_list')
  else:
    form = AuthorForm()
  return render(request, 'author_edit.html', {'form': form})

def author_delete(request, pk):
  author = get_object_or_404(Author, pk=pk)
  if request.method=='POST':
    author.delete()
    return redirect('author_list')
  return render(request, 'author_detail.html', {'author': author})

def author_edit(request, pk):
  author = get_object_or_404(Author, pk=pk)
  if request.method == "POST":
    form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
      author = form.save(commit=False)
      author.save()
      return redirect('author_detail', pk=author.pk)
  else:
    form = AuthorForm(instance=author)
  return render(request, 'author_edit.html', {'form': form})

# Genre

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genre_list': genres})

def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render (request, 'genre_detail.html', {'genre':genre})

def add_genre(request):
  if request.method == "POST":
    form = GenreForm(request.POST)
    if form.is_valid():
      genre = form.save(commit=False)
      genre.save()      
      return redirect('genre_list')
  else:
    form = GenreForm()
  return render(request, 'genre_edit.html', {'form': form})

def genre_delete(request, pk):
  genre = get_object_or_404(Genre, pk=pk)
  if request.method=='POST':
    genre.delete()
    return redirect('genre_list')
  return render(request, 'genre_detail.html', {'genre': genre})

def genre_edit(request, pk):
  genre = get_object_or_404(Genre, pk=pk)
  if request.method == "POST":
    form = GenreForm(request.POST, instance=genre)
    if form.is_valid():
      genre = form.save(commit=False)
      genre.save()
      return redirect('genre_detail', pk=genre.pk)
  else:
    form = GenreForm(instance=genre)
  return render(request, 'genre_edit.html', {'form': form})

# Genre

def publisher_list(request):
    publisher = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': publisher})

def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render (request, 'publisher_detail.html', {'publisher':publisher})

def add_publisher(request):
  if request.method == "POST":
    form = PublisherForm(request.POST)
    if form.is_valid():
      publisher = form.save(commit=False)
      publisher.save()      
      return redirect('publisher_list')
  else:
    form = PublisherForm()
  return render(request, 'publisher_edit.html', {'form': form})

def publisher_delete(request, pk):
  publisher = get_object_or_404(Publisher, pk=pk)
  if request.method=='POST':
    publisher.delete()
    return redirect('publisher_list')
  return render(request, 'publisher_detail.html', {'publisher': publisher})

def publisher_edit(request, pk):
  publisher = get_object_or_404(Publisher, pk=pk)
  if request.method == "POST":
    form = PublisherForm(request.POST, instance=publisher)
    if form.is_valid():
      publisher = form.save(commit=False)
      publisher.save()
      return redirect('publisher_detail', pk=publisher.pk)
  else:
    form = PublisherForm(instance=publisher)
  return render(request, 'publisher_edit.html', {'form': form})