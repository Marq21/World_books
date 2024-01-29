from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()

    return render(request, 'catalog/index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors},
                  )


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book
