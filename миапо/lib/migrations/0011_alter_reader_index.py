# Generated by Django 4.0.4 on 2022-04-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0010_alter_reader_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='index',
            field=models.CharField(max_length=40, verbose_name='Почтовый индекс отделения'),
        ),
    ]
