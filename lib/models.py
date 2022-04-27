from turtle import title
from django.db import models
from datetime import date

class Author(models.Model):
    """Автор книги"""
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=40)
    email = models.EmailField("Почта", null=True, unique=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Translator(models.Model):
    """Переводчик книги"""
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=40)
    email = models.EmailField("Почта", null=True, unique=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "Переводчик"
        verbose_name_plural = "Переводчики"

class Publisher(models.Model):
    """Издательство книги"""
    title = models.CharField("Название", max_length=30)
    city = models.CharField("Город", max_length=40)
    street = models.CharField("Улица", max_length=40)
    home = models.PositiveIntegerField("Дом")
    room = models.PositiveIntegerField("Квартира")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

class Genre(models.Model):
    """Жанр книги"""
    genre = models.CharField("Жанр", max_length=100)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Book(models.Model):
    AGE_LIMIT = (
        ('0+', '0+'),
        ('3+', '3+'),
        ('6+', '6+'),
        ('12+', '12+'),
        ('16+', '16+'),
        ('18+', '18+')
    )

    title = models.CharField("Название", max_length=100)
    genre = models.ForeignKey(Genre, verbose_name="Жанр", on_delete=models.SET_NULL, null=True)
    authors = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, verbose_name="Издательство", on_delete=models.SET_NULL, null=True)
    translator = models.ForeignKey(Translator, verbose_name="Переводчик", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField("Изображение", upload_to="books/")
    price = models.PositiveIntegerField("Цена", null=True, blank=True)
    date_ls = models.DateField("Дата издания", default=date.today)
    weight = models.PositiveIntegerField("Вес", null=True, blank=True)
    numb_page = models.PositiveIntegerField("Количество страниц", null=True, blank=True)
    age_limit = models.CharField("Возростное ограничение", null=True, blank=True, choices=AGE_LIMIT, max_length=3)
    annotation = models.TextField("Аннотация", null=True, blank=True)


    def __str__(self):
        return f'{self.title}----Автор:{self.authors}'

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

# class Reader(models.Model):
#     """Читатель книги"""
#     fname = models.CharField("Имя", max_length=30)
#     lname = models.CharField("Фамилия", max_length=30)
#     city = models.CharField("Город", max_length=40)
#     index = models.CharField("Почтовый индекс отделения", max_length=40, unique=True)
#     book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.SET_NULL, null=True)
#     check = models.BooleanField("Обработан", default=False)


#     def __str__(self):
#         return f'{self.lname} {self.fname}'

#     class Meta:
#         verbose_name = "Читатель"
#         verbose_name_plural = "Читатели"


# class RecordReader(models.Model):
#     """Записи книги на руки"""
#     book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.SET_NULL, null=True)
#     reader = models.ForeignKey(Reader, verbose_name="Читатель", on_delete=models.SET_NULL, null=True)
#     date = models.DateField("Дата взятия книги", default=date.today)
#     existence = models.BooleanField("На руках")

#     def __str__(self):
#         return f'{self.reader} взял на руки {self.book} {self.date}'

#     class Meta:
#         verbose_name = "Запись"
#         verbose_name_plural = "Записи"
