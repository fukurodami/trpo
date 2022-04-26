from django.contrib import admin

from . models import Author, Book, Genre, Translator, Publisher

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Translator)