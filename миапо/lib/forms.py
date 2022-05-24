from contextlib import nullcontext
from dataclasses import field
from multiprocessing.sharedctypes import Value
from tokenize import blank_re
from urllib import request
from django import forms
from .models import Reader, Book


class ReaderForm(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)
        self.fields['book'].empty_label = "Выберете книгу"

    class Meta:
        model = Reader
        fields = ['fname', 'lname', 'city', 'index', 'book']

class FilterForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, label="Фильтр")
