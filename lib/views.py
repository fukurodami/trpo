from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View

from .models import Book

class BooksView(View):
    """Список книг"""
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books.html", {"books_list": books})

class BookMailView(View):
    """Заказ книги"""
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        return render(request, "book.html", {"book": book})



