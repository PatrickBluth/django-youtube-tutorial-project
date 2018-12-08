from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from . import models, forms


def genre_list(request):
    genres = models.Genre.objects.all()
    return render(request, 'books/genre_list.html', {'genres': genres})


def book_list(request, genre):
    books = models.Book.objects.filter(genre__topic=genre)
    return render(request, 'books/book_list.html', {'books': books, 'genre': genre})


def book_detail(request, book_url, genre):
    book_title = book_url.replace('-', ' ')
    book = get_object_or_404(models.Book, genre__topic=genre, title=book_title)
    if book.title == book_url and ' ' in book_url:
        raise Http404
    return render(request, 'books/book_detail.html', {'book': book})


def book_create(request, genre):
    genre = get_object_or_404(models.Genre, topic=genre)
    form = forms.BookForm(initial={'genre': genre})

    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if 'book_save' in form.data:
            if form.is_valid():
                book = form.save(commit=False)
                book.topic = genre
                book.save()
                return HttpResponseRedirect(book.get_absolute_url())

    return render(request, 'books/book_form.html', {'form': form, 'genre': genre})


def book_edit(request, genre, book_url):
    genre = get_object_or_404(models.Genre, topic=genre)
    book_title = book_url.replace('-', ' ')
    book = get_object_or_404(models.Book, genre=genre, title=book_title)
    form = forms.BookForm(instance=book)

    if request.method == 'POST':
        form = forms.BookForm(instance=book, data=request.POST)
        if 'book_save' in form.data:
            if form.is_valid():
                book = form.save(commit=False)
                form.save()
                return HttpResponseRedirect(book.get_absolute_url())
    return render(request, 'books/book_form.html', {'form': form, 'genre': genre})
