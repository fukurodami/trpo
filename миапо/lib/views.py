from turtle import title
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from.forms import ReaderForm, FilterForm
from .models import Book, Reader

class BooksView(View):
    """Список книг"""
    def get(self, request):
        if request.method == 'POST':
            form =  FilterForm(request.POST)
            if form.is_valid():
                if form.cleaned_data["title"] != '':
                    books = Book.objects.filter(title=form.cleaned_data["title"])
        else:
            form = FilterForm()
        books = Book.objects.all()
        return render(request, "books.html", {"books_list": books, "form": form})

    def post(self, request):
        books = Book.objects.all()
        if request.method == 'POST':
            form =  FilterForm(request.POST)
            if form.is_valid():
                if form.cleaned_data["title"] != '':
                    books = Book.objects.filter(title=form.cleaned_data["title"])
        else:
            form = FilterForm()
        return render(request, "books.html", {"books_list": books, "form": form})
        

class BookMailView(View):
    """Заказ книги"""
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        if request.method == 'POST':
            form =  ReaderForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = ReaderForm()
        return render(request, "book.html", {"book": book, "form": form})
    
    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        if request.method == 'POST':
            form =  ReaderForm(request.POST)
            if form.is_valid():
                form.save()
                f = open(f"media/posts_book/{form.cleaned_data['fname']}.txt", 'w')
                f.write(f"Читатель {form.cleaned_data['fname']} {form.cleaned_data['lname']} \n")
                f.write(f"Заказ {form.cleaned_data['book']} в город {form.cleaned_data['city']} \n")
                f.write(f"Отделение {form.cleaned_data['index']}.\n")
                f.write(f"К оплате {book.price}р. + 250р за доставку")
                f.close()
                return HttpResponseRedirect('/')
        else:
            form = ReaderForm()
        return render(request, "book.html", {"book": book, "form": form})



