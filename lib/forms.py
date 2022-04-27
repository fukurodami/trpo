from django import forms

class NameForm(forms.Form):
    fname = forms.CharField(label='Your name', max_length=100)
    lname = models.CharField("Фамилия", max_length=30)
    city = models.CharField("Город", max_length=40)
    index = models.CharField("Почтовый индекс отделения", max_length=40, unique=True)
    